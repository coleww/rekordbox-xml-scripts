import xml.etree.ElementTree as ET
import sys

# https://coderrocketfuel.com/article/parse-edit-and-write-changes-to-xml-files-with-node-js#write-changes-to-the-xml-file
tree = ET.parse(sys.argv[1])
root = tree.getroot()

trackIds = []

# update this with a list of folders containing your playlists
# NOTE: this script will not traverse nested folders, or playlists that aren't in any folder
targets = ['ambientstick', 'FNCTNL', 'mixes']

for track in root.findall('./COLLECTION/TRACK'):
    trackIds.append(track.get('TrackID'))


print(len(trackIds))
for playlist in root.findall('./PLAYLISTS')[0][0]:
    if playlist.get('Name') in targets:
        for pl in playlist:
            for track in pl:
                id = track.get('Key')
                if id in trackIds:
                    trackIds.remove(id)

print(len(trackIds))

for playlist in root.findall('./PLAYLISTS')[0][0]:
    if playlist.get('Name') == 'not-in-playlist':
        for id in trackIds:
            track = ET.Element('TRACK')
            track.set('Key', id)
            playlist.append(track)


tree.write('./output.xml', encoding='UTF-8', xml_declaration=True)
