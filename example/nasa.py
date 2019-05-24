import requests
import json
import random
import ctypes
import os
from sys import argv
from windows_background_changer import WindowsBackgroundChanger

API_KEY = argv[1] if len(argv) == 2 else exit(1)

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

SEARCH = 'https://api.nasa.gov/planetary/apod?api_key={}'

o = json.loads(requests.get(SEARCH.format(API_KEY)).content)

image_url = o['hdurl']

image_title = ABS_PATH + os.sep + image_url.split('/')[-1]

with open(image_title, 'wb') as f:
    content = requests.get(image_url).content
    f.write(content)
    
WindowsBackgroundChanger.change_background(image_title)
