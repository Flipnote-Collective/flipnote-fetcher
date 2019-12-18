
import re
import json
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from sys import argv

ARCHIVE_CDX_URL = "http://web.archive.org/cdx/search/cdx?matchType=prefix&filter=original:\S*.kwz$&output=json&url=jkz-dsidata.s3.amazonaws.com/kwz/{0}"
ARCHIVE_RAW_DATA_URL = "http://web.archive.org/web/{0}id_/{1}"
HATENA_STAR_URL = "https://s.hatena.ne.jp/{0}/"
FSID_REGEX = "[0159]{1}[0-9A-F]{6}0[0-9A-F]{8}"

# Quick util to fetch a url and parse as text
def fetch(url):
  try:
    with urllib.request.urlopen(url) as response:
      if response.getcode() == 200:
        return response.read().decode()
      return None
  except:
    return None

# Fetch a list of archived Flipnotes for a given user's Flipnote Studio ID
def fetch_flipnote_list(fsid):
  return json.loads(fetch(ARCHIVE_CDX_URL.format(fsid)))

# Get raw .kwz URLS for each Flipnote in a Flipnote list
def get_flipnote_urls(flipnote_list, column_order):
  timestamp_column = column_order.index('timestamp')
  original_url_column = column_order.index('original')
  for row in flipnote_list:
    timestamp = row[timestamp_column]
    original_url = row[original_url_column]
    yield ARCHIVE_RAW_DATA_URL.format(timestamp, original_url)

# Scrape Hatena Star page for links
class HatenaStarProfileParser(HTMLParser):
  currentElement = { 'tag': None, 'attrs': [], 'text': '' }
  anchorElements = []

  def handle_starttag(self, tag, attrs):
    self.currentElement = { 'tag': tag, 'attrs': attrs, 'text': '' }
    if tag == 'a':
      self.anchorElements.append(self.currentElement)

  def handle_data(self, data):
    self.currentElement['text'] += data

# Use Hatena Star to try to find a user's Flipnote Studio ID from their given Hatena ID
# This basically scrapes their Hatena Star profile and tries to find links to their Flipnote Hatena profile there
def get_fsid_from_hatena_id(hatena_id):
  star_response = fetch(HATENA_STAR_URL.format(hatena_id))
  if star_response:
    parser = HatenaStarProfileParser()
    parser.feed(star_response)
    for element in parser.anchorElements:
      match = re.match('^うごメモはてな - .*さんの作品$', element['text'], re.I | re.M)
      if match:
        for (name, value) in element['attrs']:
          if name == 'href':
            match = re.match('^http:\/\/(?:flipnote.hatena.com|ugomemo.hatena.ne.jp)\/(' + FSID_REGEX + ')@DSi\/$', value)
            if match:
              fsid = match.groups()[0]
              return fsid
  else:
    return None

target = argv[1]
is_target_fsid = re.match('^(' + FSID_REGEX + ')$', target)

if is_target_fsid:
  target_fsid = target.upper()
else:
  target_fsid = get_fsid_from_hatena_id(target)
  if target_fsid:
    print('Matched Hatena ID: {0} to Flipnote Studio ID: {1}'.format(target, target_fsid))
  else:
    exit('Unable to match Hatena ID: {0} to a Flipnote Studio ID'.format(target))

# Fetch Flipnotes list from Web Archive + parse it
list_data = fetch_flipnote_list(target_fsid)
column_order = list_data[0] # first item provides the column order for the rest of the list
flipnote_list = list_data[1::]

# Count Flipnotes found
num_flipnotes = len(flipnote_list)
if num_flipnotes > 0:
  print("Found {0} Flipnotes for Flipnote Studio ID: {1} in Web Archive!".format(num_flipnotes, target_fsid))
else:
  print("Unable to find Flipnotes in Web Archive")

# Download if user wants to
if len(argv) == 3:
  output_dir = argv[2]
  output_path = Path(output_dir)
  output_path.mkdir(parents=True, exist_ok=True)

  for (i, flipnote_url) in enumerate(get_flipnote_urls(flipnote_list, column_order)):
    flipnote_filename = Path(flipnote_url).name
    print('Downloading Flipnote {0} of {1}'.format(i + 1, num_flipnotes))
    urllib.request.urlretrieve(flipnote_url, output_path.joinpath(flipnote_filename))

  print('Done!')