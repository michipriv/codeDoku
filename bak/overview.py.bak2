# Filename: modules/overview.py

import os
import ast


def extract_classes_funcs(file_path):
    """
    Extrahiert Klassen, Methoden und deren Parameter sowie Docstrings aus einer Python-Datei.

    Parameters:
        file_path (str): Der Pfad zur Python-Datei, die analysiert werden soll.

    Returns:
        list: Eine Liste von Dictionaries, die die Klassen, deren Methoden,
              die zugehörigen Parameter und die Docstrings enthalten.
    """
    try:
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
    except SyntaxError:
        print(f"Syntaxfehler beim Parsen der Datei: {file_path}")
        return []  # Ignoriere diese Datei bei Fehlern

    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            methods = []
            class_doc = ast.get_docstring(node)  # Extrahiere den Docstring der Klasse
            for n in node.body:
                if isinstance(n, ast.FunctionDef):
                    params = [arg.arg for arg in n.args.args]
                    method_doc = ast.get_docstring(n)
                    methods.append(
                        {"method": n.name, "params": params, "docstring": method_doc}
                    )
            classes.append(
                {"class": node.name, "docstring": class_doc, "methods": methods}
            )
    return classes


def scan_directory(path):
    """
    Durchsucht das Verzeichnis nach Python-Dateien.

    Parameters:
        path (str): Der Pfad zum Verzeichnis, das durchsucht werden soll.

    Returns:
        list: Eine Liste von Pfaden zu den gefundenen Python-Dateien.
    """
    return [
        os.path.join(root, file)
        for root, _, files in os.walk(path)
        for file in files
        if file.endswith(".py")
    ]


def generate_overview(path):
    """
    Erzeugt eine Übersicht der Klassen, Methoden, deren Parameter und Docstrings pro Datei.

    Parameters:
        path (str): Der Pfad zum Verzeichnis, das durchsucht werden soll.

    Returns:
        dict: Ein Dictionary, das die Klassen, Methoden, Parameter und Docstrings pro Datei enthält.
    """
    overview = {}
    for py_file in scan_directory(path):
        classes = extract_classes_funcs(py_file)
        if classes:
            overview[py_file] = classes
    return overview


# EOF
