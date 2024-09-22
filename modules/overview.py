# Filename: modules/overview.py
"""
Module to extract classes, methods, parameters, and docstrings from Python files.

Imports:
    - os: Provides functionalities to interact with the file system.
    - ast: Abstract Syntax Tree, used to parse Python code and extract class and function definitions.

Functions:
    - extract_classes_funcs(file_path): Extracts classes, methods, parameters, and docstrings from a Python file.
    - scan_directory(path): Scans a directory for Python files and returns a list of file paths.
    - generate_overview(path): Generates an overview of classes, methods, parameters, and docstrings from Python files in a directory.

Usage:
    overview = generate_overview(path)

Returns:
    - extract_classes_funcs: Returns a list of dictionaries containing class, method, parameter, and docstring information.
    - scan_directory: Returns a list of Python file paths in the specified directory.
    - generate_overview: Returns a dictionary mapping file paths to extracted class and method information.
"""

import os
import ast


def extract_classes_funcs(file_path):
    """
    Extracts classes, methods, parameters, and docstrings from a Python file.

    This function parses a Python file, extracting class and method definitions,
    along with their parameters and docstrings.

    Args:
        file_path (str): The path to the Python file to be analyzed.

    Returns:
        list: A list of dictionaries, each containing:
            - 'class': Name of the class.
            - 'docstring': The class docstring.
            - 'methods': A list of dictionaries, each containing:
                - 'method': Method name.
                - 'params': List of method parameters.
                - 'docstring': The method's docstring.
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
            class_doc = ast.get_docstring(node)  # Extract the class docstring
            for n in node.body:
                if isinstance(n, ast.FunctionDef):
                    params = [
                        arg.arg for arg in n.args.args
                    ]  # Extract method parameters
                    method_doc = ast.get_docstring(n)  # Extract the method docstring
                    methods.append(
                        {"method": n.name, "params": params, "docstring": method_doc}
                    )
            classes.append(
                {"class": node.name, "docstring": class_doc, "methods": methods}
            )
    return classes


def scan_directory(path):
    """
    Scans the directory for Python files.

    This function traverses the given directory and returns the paths of all Python files.

    Args:
        path (str): The directory path to scan.

    Returns:
        list: A list of file paths pointing to Python files.
    """
    return [
        os.path.join(root, file)
        for root, _, files in os.walk(path)
        for file in files
        if file.endswith(".py")
    ]


def generate_overview(path):
    """
    Generates an overview of classes, methods, parameters, and docstrings per Python file in the directory.

    This function scans the specified directory, extracts information about classes and methods from each Python file,
    and returns a structured overview.

    Args:
        path (str): The directory path to scan for Python files.

    Returns:
        dict: A dictionary where the keys are file paths and the values are lists of extracted class and method information.
    """
    overview = {}

    # Liste aller Dateien
    all_files = scan_directory(path)

    # Füge die main.py zur Liste hinzu, falls sie nicht im modules Verzeichnis ist
    main_file = os.path.join(os.path.dirname(path), "main.py")
    if os.path.exists(main_file):
        all_files.append(main_file)

    print("Gefundene Dateien:")
    for py_file in all_files:
        print(py_file)  # Debug-Ausgabe aller gefundenen Dateien

    # Erzeuge Überblick über alle gefundenen Dateien
    for py_file in all_files:
        classes = extract_classes_funcs(py_file)
        if classes:
            overview[py_file] = classes

    return overview


# EOF
