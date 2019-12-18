## Flipnote Fetcher

Fetch Flipnotes from [Flipnote Hatena](http://ugomemo.hatena.ne.jp/thankyou)... in 2019!? 👀

## Wait, What?

After [Flipnote Hatena](http://ugomemo.hatena.ne.jp/thankyou) was closed down, Nintendo converted all user-created Flipnotes to make them accessible from [Flipnote Studio 3D's](https://www.nintendo.co.uk/Games/Nintendo-3DS-download-software/Flipnote-Studio-3D-763095.html) "DSi Library" feature. DSi Library was shut down when Nintendo closed the rest of Flipnote Studio 3D's online features, and along with it all of the content from Flipnote Hatena disappeared.

Or so we thought!

Luckily for us, the amazing folks over at [Internet Archive](http://web.archive.org/) made a backup!

This project uses a super-basic Python script to interact with Internet Archive's API and fetch all of the Flipnotes from a given user's Flipnote Studio ID. These Flipnotes can then be browsed and converted to video in [Flipnote Player](https://flipnote.rakujira.jp/) or dropped onto an SD card and viewed in Flipnote Studio 3D on a Nintendo 3DS.

## Usage

Requirements:
 * Python 3, tested on version 3.7.4 but should work on other versions

To find how many Flipnotes are archived for a user's Hatena ID (e.g. id:flipnoteaardman)

```
python3 flipnote_fetcher.py flipnoteaardman
```

Or, to find how many Flipnotes are archived for a user's Flipnote Studio ID (e.g. 97849B20AA34FFBC)

```
python3 flipnote_fetcher.py 97849B20AA34FFBC
```

To download all those Flipnotes, just pass a target directory as a second param:

```
python3 flipnote_fetcher.py 97849B20AA34FFBC ./downloads
```

## Caveats

Unfortunately, we're only able to fetch Flipnotes by Flipnote Studio ID. It’s not possible to search for a specific username or Hatena ID. If you’d like those features, you might want to wait for Austin Burk’s much more comprehensive [Flipnote Archive](https://twitter.com/FlipnoteArchive) project.

We also aren't able to retrieve these Flipnotes in a format that's compatible with Flipnote Studio on the DSi.

## Credits

* [James Daniel](https://jamesdaniel.dev) for the Python implementation
* [Shutterbug2000](https://github.com/shutterbug2000) who discovered the Internet Archive backup
* [IPG](https://github.com/invoxiplaygames) for the trick used to match Hatena IDs to Flipnote Studio IDs
* [Internet Archive](http://web.archive.org/) for hosting the actual backup :)
