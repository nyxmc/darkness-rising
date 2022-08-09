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

# Load constants from file
with open("mmc-pack.json", "r") as file:
    mmc_pack = json.load(file)

for component in mmc_pack.components:
    if component.cachedName == "Minecraft":
        minecraft_version = component.version
    elif not "LWJGL" in component.cachedName or not "Mappings" in component.cachedName:
        modloader_version = component.version
        modloader = str(component.cachedName).lower().strip("loader").strip("minecraft").strip(" ")

print(minecraft_version, modloader, modloader_version)

try:
    shutil.rmtree("tmp")
except Exception as ignored:
    print("Could not remove tmp dir. Please remove it manually.")
