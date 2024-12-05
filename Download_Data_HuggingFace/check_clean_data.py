from cleanvision import Imagelab

# Specify path to folder containing the image files in your dataset
imagelab = Imagelab(data_path=r"C:\Users\Abbas Khan\Downloads\Corrosion Instance Segmentation.v16i.coco-segmentation\train\images")

imagelab.find_issues()
imagelab.report()


## soem tags ,   is_exact_duplicates_issue : is_near_duplicates_issue
problematic_images = imagelab.issues[imagelab.issues["is_near_duplicates_issue"] == True]

file_paths = problematic_images.index.tolist()

import shutil
destination_path = r'C:\Users\Abbas Khan\Downloads\Corrosion Instance Segmentation.v16i.coco-segmentation\train\dup3'
for path in file_paths:
    shutil.move(path, destination_path)
