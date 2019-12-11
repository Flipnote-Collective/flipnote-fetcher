
import json
import urllib.request
from pathlib import Path
from sys import argv

ARCHIVE_CDX_URL = "http://web.archive.org/cdx/search/cdx?matchType=prefix&filter=original:\S*.kwz$&output=json&url=jkz-dsidata.s3.amazonaws.com/kwz/{0}"
ARCHIVE_RAW_DATA_URL = "http://web.archive.org/web/{0}id_/{1}"

# Fetch a list of archived Flipnotes for a given user's Flipnote Studio ID
def fetch_flipnote_list(fsid):
  with urllib.request.urlopen(ARCHIVE_CDX_URL.format(target_fsid)) as archive_response:
    # parse list as as json
    return json.loads(archive_response.read().decode())

# Get raw .kwz URLS for each Flipnote in a Flipnote list
def get_flipnote_urls(flipnote_list, column_order):
  timestamp_column = column_order.index('timestamp')
  original_url_column = column_order.index('original')
  for row in flipnote_list:
    timestamp = row[timestamp_column]
    original_url = row[original_url_column]
    yield ARCHIVE_RAW_DATA_URL.format(timestamp, original_url)

# Fetch Flipnotes list from Web Archive + parse it
target_fsid = argv[1].upper()
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