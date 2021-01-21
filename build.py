import json
import os
import re

han_regex = re.compile(r'[\u3006\u3007\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002b73f\U0002b740-\U0002b81f\U0002b820-\U0002ceaf\U0002ceb0-\U0002ebef\U00030000-\U0003134f]+')

# Library
os.system('wget -nc -O lib/browser-polyfill.js https://unpkg.com/webextension-polyfill@0.6.0/dist/browser-polyfill.js')

# Resources
os.system('wget -nc -O content_scripts/FiraXdi8Variable-subset.woff2 https://cdn.jsdelivr.net/gh/edward-martyr/syyon-vencie@2f449da/Fira%20Xdi8%20Variable-subset.woff2')
os.system('cp content_scripts/FiraXdi8Variable-subset.woff2 popup/FiraXdi8Variable-subset.woff2')

# Preprocess
os.system('wget -nc https://raw.githubusercontent.com/edward-martyr/Xdi8Translator/b5486a1/Xdi8Translator/data.py')

with open('data.py') as f:
	exec(f.read())

l = []

for k, v in hanzi2xdi8_dict.items():
	if han_regex.fullmatch(k): # remove non-Han characters
		l.append((k, v))

with open('background_scripts/dictionary.json.txt', 'w') as f: # *.json.txt: See mozilla/addons-linter#1700
	f.write(json.dumps(l, ensure_ascii=False).replace('], [', '],\n['))
	f.write('\n') # add line break at the end of file
