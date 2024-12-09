import os
import shutil

def copy_images(folder1, folder2):
    # Ensure folder2 exists
    if not os.path.exists(folder2):
        os.makedirs(folder2)
    
    # Supported image extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    
    # Get the list of image files in folder1
    image_files = [f for f in os.listdir(folder1) if f.lower().endswith(image_extensions)]
    
    # Copy each image to folder2
    for image in image_files:
        src_path = os.path.join(folder1, image)
        dst_path = os.path.join(folder2, image)
        shutil.copy(src_path, dst_path)
    
    # Print the total count of images
    print(f"Total number of images in '{folder1}': {len(image_files)}")


data_names = [
    "c1_Corrosion Condition State Classification",
    "c2_Corrosion Instance Segmentation.v16i",
    "c3_corrosion-in-industrial-complexes-in-ostrava",
    "c4_dataset3_Rust Detection.v3i.png-mask-semantic",
    "c5_Kaggle_corrosion-annotated",
    "c6_rkumaricorrosion_segment",
    "c7_Marine Vessel Hull Corrosion",
    "c8_Nut and bolt corrosion 2.v1i.coco-segmentation",
    "c9_rfyuf_kaggle_rust-segmentation"
]

for data_name in data_names:

    folder1 = r"C:\Users\Abbas Khan\Downloads\Data_Downloaded/"+data_name+"/train\imgs"
    folder2 = r"D:\train\imgs"  # Replace with the path to folder2
    copy_images(folder1, folder2)
    
    folder1 = r"C:\Users\Abbas Khan\Downloads\Data_Downloaded/"+data_name+"/train\gts"
    folder2 = r"D:\val\gts"  # Replace with the path to folder2
    copy_images(folder1, folder2)



# total_file_count = 0



# all_names = []

# print()
# image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
# for data_name in data_names:
#     folder1 = r"C:\Users\Abbas Khan\Downloads\Data_Downloaded/"+data_name+"/train\imgs"
#     image_files = [f for f in os.listdir(folder1) if f.lower().endswith(image_extensions)]
    
#     all_names.append(image_files)
    
#     total_file_count += len(image_files)
    
#     print(data_name, '    -->',len(image_files))


# combined_list = [item for sublist in all_names for item in sublist]

# unique = set(combined_list)

# from collections import Counter
# # Example list
# # Count occurrences of each element
# counter = Counter(combined_list)
# # Find entries that appear more than once
# duplicates = [item for item, count in counter.items() if count > 1]
# print(f"Entries that appear more than once: {duplicates}")


