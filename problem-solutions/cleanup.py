# Make the folder CleanedUp/
# List the files in the Desktop/ folder
# For each file in the Desktop/ folder
    # Move the file to the Cleanedup/ folder

import os

folder_original = '/home/xlopez/Desktop'
folder_destination = '/home/xlopez/Desktop/CleanedUp/'

if not os.path.exists(folder_destination):
    os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)
