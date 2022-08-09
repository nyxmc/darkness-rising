import requests
import json
import os

from murmurhash2 import murmurhash2
from utils import zip, create_tmp_dir, delete_tmp_dir, murmur64

# create temp dir
create_tmp_dir("tmp")

# Constants
api_url = "https://api.curse.tools/v1/cf"
pack_author = ""
minecraft_version = ""
modloader = ""
modloader_version = ""
includes = []
headers = { "Content-Type": "application/json", "Accept": "application/json" }

# Load constants from mmc config
with open("mmc-pack.json", "r") as file:
    mmc_pack = json.load(file)

    for component in mmc_pack["components"]:
        if component["cachedName"] == "Minecraft":
            minecraft_version = component["version"]
        elif not "LWJGL" in component["cachedName"] or not "Mappings" in component["cachedName"]:
            modloader_version = component["version"]
            modloader = str(component["cachedName"]).lower().replace("loader", "").replace("minecraft", "").replace(" ", "")

# Get all mod hashes
mod_hashes = []
for root, directories, files in os.walk(".minecraft/mods"):
    for path in files:
        with open(os.path.join(root, path), "rb") as file:
            hash = murmur64(file), 1)
            mod_hashes.append(hash)

# Get project ids from hashes
body = { "fingerprints": mod_hashes }
res = requests.post(api_url + "/fingerprints", headers=headers, data=body)
print(res.json())

# Create zip
#zip("Darkness_Rising_CF.zip", ["tmp"])

# Remove temp dir when done
delete_tmp_dir("tmp")
