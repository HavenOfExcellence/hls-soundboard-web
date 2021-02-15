from pathlib import Path
from pprint import pprint

print('[HLS CLI] Generating sound paths')

p = Path("static/sounds/")
sounds = []

for i in p.glob('**/*.mp3'):
    sound_path = str(i).split("sounds")[1]

    # Make sure not system file not .DS_Store
    if not (sound_path[0] == "."):

        filename = sound_path.split('/')[1]

        try: sounds.append(filename)
        except: sounds = [filename]

sounds.sort()

print('[HLS CLI] Writing to `content/sounds.js` ...')

# Write to ../contents/sounds.js
file = open('contents/sounds.js', 'w')
file.write(f"export let sounds = {str(sounds)};\n" )
file.close()

print('[HLS CLI] Complete!')