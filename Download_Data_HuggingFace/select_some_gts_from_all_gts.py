import os
import shutil

# Define the paths to the image and mask folders
image_folder = r'C:\Users\Abbas Khan\Downloads\Data_Downloaded\dataset3_Rust Detection.v3i.png-mask-semantic\train\imgs'
mask_folder = r'C:\Users\Abbas Khan\Downloads\Data_Downloaded\dataset3_Rust Detection.v3i.png-mask-semantic\train\gts_all'
output_folder = r'C:\Users\Abbas Khan\Downloads\Data_Downloaded\dataset3_Rust Detection.v3i.png-mask-semantic\train\gts'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all the image files in the image folder (only .jpg files)
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

# Loop through each image file
for image_file in image_files:
    # Construct the corresponding mask file name by replacing .jpg with .png
    mask_file = image_file.replace('.jpg', '_mask.png')  ## _mask --> added
    
    # Check if the corresponding mask exists in the mask folder
    mask_path = os.path.join(mask_folder, mask_file)
    if os.path.exists(mask_path):
        # Construct the destination path for the mask
        destination_path = os.path.join(output_folder, mask_file)
        
        # Move the mask file to the output folder
        shutil.move(mask_path, destination_path)
        print(f"Moved: {mask_file}")
    else:
        print(f"Mask not found for: {image_file}")

print("Process complete.")
