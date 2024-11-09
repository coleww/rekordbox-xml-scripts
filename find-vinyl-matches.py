import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.argv[1])
root = tree.getroot()
keybeeps = {}


transpos = [0.94387, 1.0, 1.05946]

minorKeys = ['Am', 'Bbm', 'Bm', 'Cm', 'Dbm', 'Dm', 'Ebm', 'Em', 'Fm', 'F#m', 'Gm', 'Abm']
majorKeys = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab']


def isMinorKey(key):
  return key.endswith('m')

def getKeys(key):
  if isMinorKey(key):
    return minorKeys
  else:
    return majorKeys


def getMapKey(b, k):
  return  "%s %s"%(round(b, 2), k)

def incrementKey(key):
  keys = getKeys(key)
  currentIndex = keys.index(key)
  newIndex = currentIndex + 1
  if newIndex >= len(keys):
    newIndex = 0
  return keys[newIndex]


def decrementKey(key):
  keys = getKeys(key)
  currentIndex = keys.index(key)
  newIndex = currentIndex - 1
  if newIndex < 0:
    newIndex = 11
  return keys[newIndex]

for track in root.findall('./COLLECTION/TRACK'):
  id = track.get('TrackID')
  key = track.get('Tonality')
  bpm = track.get('AverageBpm')
  
  for transpo in transpos:
    newBpm = float(bpm) * transpo
    if (transpo > 1):
      newKey = incrementKey(key)
    elif (transpo < 1):
      newKey = decrementKey(key)
      # print(key, newKey)
    else:
      newKey = key  
    
    mapKey = getMapKey(newBpm, newKey)

    if mapKey in keybeeps:
      keybeeps[mapKey].append(id)
    else:
      keybeeps[mapKey] = [id]




print(dict(sorted(keybeeps.items(), key=lambda item: len(item[1]))))

# TODO: for keybeeps entries that meet certain criteria (number of entries?) create playlist


# given a BPM and a key
# calculate what the BPM would be when moving up/down whole notes
# but staying within reasonably vinyl bounds
# store results in dictionary
# return sorted by why BPM/key combo has the most matches


# root is 120


# +1 increment
# bpm	127.136
# % change	5.946

# -1 down 1 step
# bpm	113.265
# % change	-5.613