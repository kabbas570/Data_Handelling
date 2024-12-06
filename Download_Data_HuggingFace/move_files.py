import os
import shutil

# Paths to the source and destination folders
folder1 = r"C:\Users\Abbas Khan\Downloads\rfyuf_kaggle_rust-segmentation\test"
folder2 = r"C:\Users\Abbas Khan\Downloads\rfyuf_kaggle_rust-segmentation\New folder"

# Ensure the destination folder exists

# Iterate through all files in folder1
for file_name in os.listdir(folder1):
    # Check if the file name contains '_mask'
    if '_mask' in file_name:
        # Construct full file paths
        src_path = os.path.join(folder1, file_name)
        dest_path = os.path.join(folder2, file_name)

        # Move the file to folder2
        shutil.move(src_path, dest_path)
        #print(f"Moved: {file_name}")

print("All matching files have been moved.")
