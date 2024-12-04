from datasets import load_dataset
import os
from PIL import Image

# Download the "rkumari/corrosion_segment" dataset, train split

segmentation_dataset = load_dataset("rkumari/corrosion_segment", split="validation")


# Access images and masks (assuming the dataset structure includes "image" and "labe" keys)
# These key might be different for each dataset 

# Define output directories
output_image_dir = r"C:\Users\Abbas Khan\Downloads\Data_Downloaded\rkumaricorrosion_segment\val\imgs"
output_mask_dir = r"C:\Users\Abbas Khan\Downloads\Data_Downloaded\rkumaricorrosion_segment\val\gts"


# Save images and masks using index
for i, sample in enumerate(segmentation_dataset):
    image = sample["image"]  # Key for the image
    mask = sample["label"]   # Key for the mask

    # Convert to PIL Image if necessary
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)

    if not isinstance(mask, Image.Image):
        mask = Image.fromarray(mask)

    # Save image and mask
    image.save(os.path.join(output_image_dir, f"image_{i}.png"))
    mask.save(os.path.join(output_mask_dir, f"mask_{i}.png"))

    print(f"Saved: image_{i}.png and mask_{i}.png")

