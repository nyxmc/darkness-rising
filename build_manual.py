import os
from zipfile import ZipFile

os.mkdir("build")

with ZipFile("build/Darkness_Rising_Manual.zip", mode="w") as archive:  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(".minecraft/mods"):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            archive.write(filepath)
  
        