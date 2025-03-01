# Filename: modules/generator.py

import os
import ast


class OverviewGenerator:
    def __init__(self, project_path):
        """
        Initializes the OverviewGenerator with the provided project path.

        Args:
            project_path (str): The directory path where the project files are located.
        """
        self.project_path = project_path

    def generate_overview(self, file_list):
        """
        Generates an overview of classes, methods, and functions from all Python files in the given project path.
        Uses the provided file list to ensure all files are documented, even if they contain no classes or methods.

        Args:
            file_list (list): The list of Python files to document.

        Returns:
            dict: A dictionary where the keys are file paths and the values are lists of extracted class, method, and function information.
        """
        overview = {}

        for py_file in file_list:
            classes_and_functions = self._extract_classes_funcs(py_file)
            # Füge die Datei auch hinzu, wenn keine Klassen/Methoden/Funktionen gefunden wurden
            overview[py_file] = (
                classes_and_functions
                if classes_and_functions
                else ["Keine Dokumentation"]
            )

        return overview

    def scan_directory(self):
        """
        Scans the project directory for Python files.
        This function traverses the given project directory and returns the paths of all Python files.
        """
        return [
            os.path.join(root, file)
            for root, _, files in os.walk(self.project_path)
            for file in files
            if file.endswith(".py")
        ]

    def _extract_classes_funcs(self, file_path):
        """
        Extracts classes, methods, parameters, and docstrings from a Python file.
        Also extracts top-level functions outside of classes.

        Args:
            file_path (str): The path to the Python file to be analyzed.

        Returns:
            list: A list of dictionaries containing class and method information, or function information.
        """
        try:
            with open(file_path, "r") as f:
                tree = ast.parse(f.read())
        except (SyntaxError, IsADirectoryError):
            print(f"Fehler beim Parsen der Datei: {file_path}")
            return []

        result = []

        # Sammle alle Klassen und deren Methoden
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):  # Suche nach Klassen
                methods = []
                class_doc = ast.get_docstring(node)  # Hole den Docstring der Klasse
                for n in node.body:
                    if isinstance(
                        n, ast.FunctionDef
                    ):  # Suche nach Methoden in der Klasse
                        params = [arg.arg for arg in n.args.args]
                        method_doc = ast.get_docstring(
                            n
                        )  # Hole den Docstring der Methode
                        methods.append(
                            {
                                "method": n.name,
                                "params": params,
                                "docstring": method_doc,
                            }
                        )
                result.append(
                    {"class": node.name, "docstring": class_doc, "methods": methods}
                )

            elif isinstance(
                node, ast.FunctionDef
            ):  # Suche nach Funktionen auf Modulebene
                params = [arg.arg for arg in node.args.args]
                func_doc = ast.get_docstring(node)  # Hole den Docstring der Funktion
                result.append(
                    {"function": node.name, "params": params, "docstring": func_doc}
                )

        return result
