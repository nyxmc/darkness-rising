import os
from zipfile import ZipFile

os.mkdir("build")

with ZipFile("build/Darkness_Rising_MMC.zip", mode="w") as archive:
    archive.write("mmc-pack.json")
    archive.write("instance.cfg")

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(".minecraft"):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            archive.write(filepath)
  
        