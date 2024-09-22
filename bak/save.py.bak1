# Filename: modules/save.py


def save_as_md(overview, output_file):
    """
    Speichert die Übersicht in einer menschenlesbaren Markdown-Datei.

    Parameters:
        overview (dict): Die Übersicht der Klassen, Methoden und Parameter.
        output_file (str): Der Pfad zur Ausgabedatei.
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
    Speichert die Übersicht in einer HTML-Datei.

    Parameters:
        overview (dict): Die Übersicht der Klassen, Methoden und Parameter.
        output_file (str): Der Pfad zur Ausgabedatei.
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


# EOF
