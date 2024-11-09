import xml.etree.ElementTree as ET
import sys
from itertools import product

tree = ET.parse(sys.argv[1])
root = tree.getroot()



intelligentPlaylists = {}


# replace these with whatever bpms you play at. My collection has BPM analyzed so everything is >=90 and <= 180
bpms = [160, 140, 130, 120, 100]
genres = ['house', 'ambient', 'Techno', 'breaks', 'ravy', 'wub', 'decon', 'dub', 'trancy']
vibes = ['80s', '90s', 'horney', 'poundy', 'wiggly', 'emotional' 'lysergic', 'pop', 'acid', 'tracky', 'chill', 'aggro', 'silly', 'shady', 'beauty', 'hazy', 'FUN']

def get_bpm_match(bpm):
  for targetBpm in bpms:
    if int(bpm.split('.')[0]) in range(targetBpm - 12, targetBpm + 12):
      return targetBpm



def get_comment_match(comments, target):
  for thing in target:
    if thing in comments:
      return thing

def get_genre(possibleGenre):
  if possibleGenre in genres:
    return possibleGenre


def get_vibe(possibleVibe):
  if possibleVibe in vibes:
    return possibleVibe
for track in root.findall('./COLLECTION/TRACK'):
    bpm = track.get('AverageBpm')
    tags = track.get('Comments').replace('*', '').replace(' ', '').split('/')

    bpmMatch = get_bpm_match(bpm)
    genreMatch = get_comment_match(tags, genres)
    vibeMatch = get_comment_match(tags, vibes)


    genreMatches = filter(get_genre, tags)
    vibeMatches = filter(get_vibe, tags)

    if bpmMatch and genreMatch and vibeMatch:
      # print('got one')
      for guys in product(genreMatches, vibeMatches):
        # print(guys)
        playlistKey = "%s %s %s"%(bpmMatch, guys[0], guys[1])
        if playlistKey in intelligentPlaylists:
          intelligentPlaylists[playlistKey] += 1
        else:
          intelligentPlaylists[playlistKey] = 1
          


print(dict(sorted(intelligentPlaylists.items(), key=lambda item: item[1])))
    # if tags contains a genre and vibe, add this track to a list for the BPM/GENRE/VIBE combo
    # WE DO NOT need to actually create the playlist because making an intelligent playlist is way smarter



