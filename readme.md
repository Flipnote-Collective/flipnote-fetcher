# NOTE

> This has been deprecated in favour of the [Flipnote Archive](https://archive.sudomemo.net/) project, a comprehensive archive of Flipnote Hatena that you can view in a web browser.

----

## Flipnote Fetcher

Fetch Flipnotes from [Flipnote Hatena](http://ugomemo.hatena.ne.jp/thankyou)... in 2021!? 👀

## Wait, What?

After [Flipnote Hatena](http://ugomemo.hatena.ne.jp/thankyou) was closed down, Nintendo converted all user-created Flipnotes to make them accessible from [Flipnote Studio 3D's](https://www.nintendo.co.uk/Games/Nintendo-3DS-download-software/Flipnote-Studio-3D-763095.html) "DSi Library" feature. DSi Library was shut down when Nintendo closed the rest of Flipnote Studio 3D's online features, and along with it all of the content from Flipnote Hatena disappeared.

Or so we thought!

Luckily for us, a partial backup was saved with the amazing folks over at [Internet Archive](http://web.archive.org/)!

This project uses a super-basic Python script to interact with Internet Archive's API and fetch all of the Flipnotes from a given user's Flipnote Studio ID. These Flipnotes can then be browsed and converted to video in [Flipnote Player](https://flipnote.rakujira.jp/) or dropped onto an SD card and viewed in Flipnote Studio 3D on a Nintendo 3DS.

## Usage

Requirements:
 * Python 3, tested on version 3.7.4 but should work on other versions

To find how many Flipnotes are archived for a user's Flipnote Studio ID (e.g. 97849B20AA34FFBC)

```
python3 flipnote_fetcher.py 97849B20AA34FFBC
```

To download all those Flipnotes, just pass a target directory as a second param:

```
python3 flipnote_fetcher.py 97849B20AA34FFBC ./downloads
```

## Caveats

Unfortunately, we're only able to fetch Flipnotes by Flipnote Studio ID. It’s not possible to search for a specific username, and since Hatena [removed old Hatena Star functionality in October of 2020](https://star.hatenastaff.com/entry/2020/10/13/171101), it's no longer possible to search by Hatena ID either. We also aren't able to retrieve these Flipnotes in a format that's compatible with Flipnote Studio on the DSi.

The archive we're pulling from also only contains a small portion of the data from Flipnote Hatena; around 476,300 Flipnotes out of 44,351,673 in total.

If you’d like more features, and a complete dataset, and you might want to wait for Austin Burk’s much more comprehensive [Flipnote Archive](https://twitter.com/FlipnoteArchive) project.

Additionally, lots of the Flipnotes unfortunately had audio issues introduced during Nintendo's conversion process to Flipnote Studio 3D format due to a bug on their end; for more details and a tool which does its best to correct the issue, see our [kwz-restoration](https://github.com/Flipnote-Collective/kwz-restoration) project. (Recent versions of Flipnote.js, as used in Flipnote Player and the Kaeru Gallery website, automatically try to spot and compensate for the issue in real-time)

## Credits

* [James Daniel](https://jamesdaniel.dev) for the Python implementation
* [Shutterbug2000](https://github.com/shutterbug2000) who discovered the Internet Archive backup
* [IPG](https://github.com/invoxiplaygames) for the trick used to match Hatena IDs to Flipnote Studio IDs
* [Internet Archive](http://web.archive.org/) for hosting the actual backup :)
* [Meemo4556](https://github.com/meemo) and [SimonTime](https://github.com/SimonTime) for helping to figure out the audio issues.
