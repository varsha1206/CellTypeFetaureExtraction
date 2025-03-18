import nbformat

# Load the notebook
with open(r"C:\Users\Varsha\OneDrive\Documents\Github\cellType\cHL_2_MIBI\cell_crops.ipynb", "r") as file:
    notebook = nbformat.read(file, as_version=4)

# Save the notebook again
with open("extracting_cell_crops.ipynb", "w") as file:
    nbformat.write(notebook, file)