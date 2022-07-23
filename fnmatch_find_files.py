# fnmatch

import fnmatch
import os

FilePath = '/'
pattern = '*.mp3'

# Search for all mp3 files

for root, dirs, files in os.walk(FilePath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))


# Search for all images

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk("C:\"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))
