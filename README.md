# rekordbox scripts


scripts for doing fun stuff with rekordbox. some of these just output information that you can use, some create playlists or modify tracks that can then be re-imported to your collection.

originally forked from https://github.com/diracdeltas/rekordbox-scripts

## prereqs

* [rekordbox](https://rekordbox.com/en/)
* [python3](https://www.python.org/downloads/)

## usage

### exporting your rekordbox collection as XML

in Rekordbox select `File` and then `Export Collection in xml format`.

### running

`python3 SCRIPT_NAME.py PATH_TO_YOUR_XML.xml`

#### scripts

- find-biggest-artist.py: Finds which artists you have the most tracks from. I love to remove tracks from my collection and constantly refine down to my favorite tracks from a given artist/genre/era/etc.
- find-tag-combos.py: Tries to find which combinations of BPM (+/-10bpm) and tags you have the most of. Returns data you can use to create intelligent playlists. May or may not be useful depending on how you tag tracks. 
- find-vinyl-matches.py: Tries to find tracks that will be in the exact same key when played at the exact same BPM on vinyl with no pitch correction.
- not-in-playlist.py: Given a list of playlist folders, it creates a new playlist of tracks that aren't in any of the playlists in that folder. Creates an output.xml file to import the `not-in-playlist` playlist. 


### importing the modified collection back into Rekordbox

1. in rekordbox, choose `Preferences`, `Advanced` and then `Database`.
2. click on the `Browse` button, find output.xml and click open.
3. choose `Preferences`, `View`, and then check `rekordbox xml` in `Layout`.
4. rekordbox xml appears in your browser window. expand and click `All Tracks`
5. select the track(s) that you want to import and right click and select `Import to Collection`. Or drag over playlists that were created.

