import os

# Paths to the two folders
folder1 = r"C:\Users\Abbas Khan\Downloads\Data_Downloaded\dataset3_Rust Detection.v3i.png-mask-semantic\train\imgs"
folder2 = r"C:\Users\Abbas Khan\Downloads\Data_Downloaded\dataset3_Rust Detection.v3i.png-mask-semantic\train\gts"

# Function to get image names without extensions
def get_image_names_without_extension(folder_path):
    return {os.path.splitext(image)[0] for image in os.listdir(folder_path)}

def get_image_names_without_extension2(folder_path):
    return {os.path.splitext(image)[0][:-5] for image in os.listdir(folder_path)}

# Get image names from both folders
images_folder1 = get_image_names_without_extension(folder1)
images_folder2 = get_image_names_without_extension2(folder2)

# Find images present in folder1 but not in folder2
unique_to_folder1 = images_folder1 - images_folder2

# Print the result
print("Images present in folder1 but not in folder2:")
for image in unique_to_folder1:
    print(image)
