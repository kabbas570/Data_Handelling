from cleanvision import Imagelab

# Specify path to folder containing the image files in your dataset
imagelab = Imagelab(data_path=r"C:\Users\Abbas Khan\Downloads\Data_Downloaded\rkumaricorrosion_segment\val\imgs/")

# Automatically check for a predefined list of issues within your dataset
imagelab.find_issues()

# Produce a neat report of the issues found in your dataset
imagelab.report()
