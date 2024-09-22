#Filename: modules/save.py
"""
Module to save the overview of classes, methods, parameters, and docstrings in Markdown and HTML formats.

Functions:
    - save_as_md(overview, output_file): Saves the overview as a readable Markdown file.
    - save_as_html(overview, output_file): Saves the overview as an HTML file.

Usage:
    save_as_md(overview, output_file)
    save_as_html(overview, output_file)

Parameters:
    - overview (dict): A dictionary containing class, method, parameter, and docstring information for each file.
    - output_file (str): The path to the output file where the overview will be saved.
"""

def save_as_md(overview, output_file):
    """
    Saves the overview as a human-readable Markdown file.

    This function formats the overview of classes, methods, parameters, and docstrings 
    and writes it to a Markdown file. The file contains hierarchical headers for files, classes, and methods.

    Args:
        overview (dict): The overview of classes, methods, and parameters. Each key is a file path, and the value is a list of class information.
        output_file (str): The path to the Markdown file where the overview will be saved.

    Returns:
        None
    """
    with open(output_file, "w") as f:
        for file_path, classes in overview.items():
            f.write(f"# Datei: {file_path}\n")
            for cls in classes:
                f.write(f"  ## Klasse: {cls['class']}\n")
                if cls["docstring"]:
                    f.write(f"    Docstring: {cls['docstring']}\n")
                for method in cls["methods"]:
                    params_str = ", ".join(method["params"])
                    f.write(f"    ### Methode: {method['method']}({params_str})\n")
                    if method["docstring"]:
                        f.write(f"      Docstring: {method['docstring']}\n")
            f.write("\n")


def save_as_html(overview, output_file):
    """
    Saves the overview as an HTML file.

    This function formats the overview of classes, methods, parameters, and docstrings 
    and writes it to an HTML file. The output is structured with headers for files, classes, and methods.

    Args:
        overview (dict): The overview of classes, methods, and parameters. Each key is a file path, and the value is a list of class information.
        output_file (str): The path to the HTML file where the overview will be saved.

    Returns:
        None
    """
    with open(output_file, "w") as f:
        f.write("<html><body>\n")
        f.write("<h1>Klassenübersicht</h1>\n")
        for file_path, classes in overview.items():
            f.write(f"<h2>Datei: {file_path}</h2>\n")
            for cls in classes:
                f.write(f"<h3>Klasse: {cls['class']}</h3>\n")
                if cls["docstring"]:
                    f.write(f"<p>Docstring: {cls['docstring']}</p>\n")
                for method in cls["methods"]:
                    params_str = ", ".join(method["params"])
                    f.write(f"<p>Methode: {method['method']}({params_str})</p>\n")
                    if method["docstring"]:
                        f.write(f"<p>Docstring: {method['docstring']}</p>\n")
        f.write("</body></html>")

#EOF
