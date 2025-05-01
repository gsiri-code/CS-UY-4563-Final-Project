import nbformat
from nbformat.v4 import new_notebook

def merge_notebooks(notebook_paths, output_path):
    merged_nb = new_notebook()
    merged_cells = []

    for path in notebook_paths:
        with open(path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            merged_cells.extend(nb.cells)

    merged_nb.cells = merged_cells

    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(merged_nb, f)

    print(f"Merged notebook saved to {output_path}")

# Example usage
notebooks_to_merge = ["kmeans.ipynb", "reg.ipynb", "svr.ipynb", "nn.ipynb"]
output_notebook = "merged_notebook.ipynb"

merge_notebooks(notebooks_to_merge, output_notebook)