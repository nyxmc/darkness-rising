import requests

import json
import os
import shutil

os.mkdir("tmp")
os.mkdir("build")

# Constants
api_url = "https://api.curse.tools/v1/cf"
pack_author = ""
minecraft_version = ""
modloader = ""
modloader_version = ""
includes = []

try:
    shutil.rmtree("tmp")
except Exception as ignored:
    print("Could not remove tmp dir. Please remove it manually.")
