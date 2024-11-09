import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.argv[1])
root = tree.getroot()
names = {}

# Find which artist you have the most tracks from
# if i have like a dozen+ tracks from the same artist, maybe i should curate that down further? 

for track in root.findall('./COLLECTION/TRACK'):
    name = track.get('Artist')
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

print(dict(sorted(names.items(), key=lambda item: item[1])))