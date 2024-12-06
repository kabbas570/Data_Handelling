from cleanvision import Imagelab
import shutil
# Specify path to folder containing the image files in your dataset

data_path = r"C:\Users\Abbas Khan\Downloads\Data_Downloaded\dataset3_Rust Detection.v3i.png-mask-semantic\valid\imgs"
imagelab = Imagelab(data_path=data_path)

imagelab.find_issues()
imagelab.report()


## soem tags ,   is_exact_duplicates_issue : is_near_duplicates_issue
problematic_images = imagelab.issues[imagelab.issues["is_near_duplicates_issue"] == True]
file_paths = problematic_images.index.tolist()


destination_path = r'C:\Users\Abbas Khan\Downloads\Data_Downloaded\dataset3_Rust Detection.v3i.png-mask-semantic\valid\dup'
for path in file_paths:
    shutil.move(path, destination_path)
    
    
import imagehash
from PIL import Image
import os
import shutil

# Path to the folder containing images
duplicate_folder = r'C:\Users\Abbas Khan\Downloads\Data_Downloaded\dataset3_Rust Detection.v3i.png-mask-semantic\valid\dup'

# Function to compute image hash
def get_image_hash(image_path):
    with Image.open(image_path) as img:
        return imagehash.phash(img)

# Create a dictionary to store image hashes
image_hashes = {}
duplicates = []

# Loop through each image in the folder
for file_name in os.listdir(duplicate_folder):
    file_path = os.path.join(duplicate_folder, file_name)
    image_hash = get_image_hash(file_path)
    
    # Check if this hash already exists
    if image_hash in image_hashes:
        duplicates.append(file_path)
    else:
        image_hashes[image_hash] = file_path

# Delete the duplicates (keep one)
for duplicate in duplicates:
    os.remove(duplicate)
    print(f"Deleted: {duplicate}")
    
    
