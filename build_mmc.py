import os
from zipfile import ZipFile


with ZipFile("build/Darkness_Rising_MMC.zip", mode="w") as archive:
        file_paths = ["instance.cfg", "mmc-pack.json"]
  
        # crawling through directory and subdirectories
        for root, directories, files in os.walk(".minecraft"):
            for filename in files:
                # join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        
        with ZipFile('build/Darkness_Rising_MMC.zip','w') as zip:
            for file in file_paths:
                 zip.write(file)
  
        