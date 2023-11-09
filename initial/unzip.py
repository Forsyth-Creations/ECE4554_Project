# download a zip from this link
# https://public.roboflow.com/classification/rock-paper-scissors/1/download

import zipfile
import os

# extract the zip file
with zipfile.ZipFile("dataset.zip", 'r') as zip_ref:
    zip_ref.extractall("dataset")

# remove the zip file
os.system("rm rock-paper-scissors.zip")

# rename the folder
os.system("mv rock-paper-scissors dataset")