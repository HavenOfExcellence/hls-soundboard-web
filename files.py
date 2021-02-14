import os
import glob
from pathlib import Path
from pprint import pprint

p = Path("static/sounds/")
sounds = []

for i in p.glob('**/*.mp3'):
  sound_path = str(i).split("sounds")[1]

  # make sure not system file
  if not (sound_path[0] == "."):
    
    filename = sound_path.split('/')[0]

    try: sounds.append(filename)
    except: sounds = [filename]


# pprint(sounds)

# write to ../contents/sounds.js
file = open('contents/sounds.js', 'w')
file.write(f"export let sounds = {str(sounds)};\n" )
file.close()

print("Done.")