# Filename: modules/overview_saver.py

import json  # Importiere json für die JSON-Ausgabe


class OverviewSaver:
    def __init__(self, overview, file_list):
        """
        Initializes the OverviewSaver with the project overview data and the list of all files.

        Args:
            overview (dict): The overview of classes, methods, and functions. Each key is a file path, and the value is a list of class and function information.
            file_list (list): The list of all Python files to ensure all are documented.
        """
        self.overview = overview
        self.file_list = file_list

    def save_overview_as_md(self, output_file):
        """
        Saves the overview of classes, methods, and functions as a Markdown file.
        Files with no documentation will be indicated.

        Args:
            output_file (str): The path to the Markdown file where the overview will be saved.

        Returns:
            None
        """
        with open(output_file, "w") as f:
            f.write("# Übersicht der gescannten Dateien\n\n")

            # Liste alle Dateien auf
            for file_path in self.file_list:
                f.write(f"- {file_path}\n")

            f.write("\n# Dokumentation der Dateien\n\n")

            # Schreibe die Dokumentation für jede Datei
            for file_path in self.file_list:
                f.write(f"# Datei: {file_path}\n")
                if file_path in self.overview and self.overview[file_path]:
                    # Dokumentation der Klassen, Methoden und Funktionen
                    for item in self.overview[file_path]:
                        if isinstance(item, dict):
                            if "class" in item:
                                f.write(f"  ## Klasse: {item['class']}\n")
                                if item["docstring"]:
                                    f.write(f"    Docstring: {item['docstring']}\n")
                                for method in item["methods"]:
                                    params_str = ", ".join(method["params"])
                                    f.write(
                                        f"    ### Methode: {method['method']}({params_str})\n"
                                    )
                                    if method["docstring"]:
                                        f.write(
                                            f"      Docstring: {method['docstring']}\n"
                                        )
                            elif "function" in item:
                                params_str = ", ".join(item["params"])
                                f.write(
                                    f"  ## Funktion: {item['function']}({params_str})\n"
                                )
                                if item["docstring"]:
                                    f.write(f"    Docstring: {item['docstring']}\n")
                        else:
                            f.write(f"  {item}\n")
                else:
                    f.write("  Keine Dokumentation\n\n")

    def save_overview_as_html(self, output_file):
        """
        Saves the overview of classes, methods, and functions as an HTML file.
        Files with no documentation will be indicated.

        Args:
            output_file (str): The path to the HTML file where the overview will be saved.

        Returns:
            None
        """
        with open(output_file, "w") as f:
            f.write("<html><body>\n")
            f.write("<h1>Übersicht der gescannten Dateien</h1>\n<ul>\n")

            # Liste aller Dateien
            for file_path in self.file_list:
                f.write(f"<li>{file_path}</li>\n")

            f.write("</ul>\n<h2>Dokumentation der Dateien</h2>\n")

            # Dokumentation der Dateien
            for file_path in self.file_list:
                f.write(f"<h3>Datei: {file_path}</h3>\n")
                if file_path in self.overview and self.overview[file_path]:
                    # Dokumentation der Klassen, Methoden und Funktionen
                    for item in self.overview[file_path]:
                        if isinstance(item, dict):
                            if "class" in item:
                                f.write(f"<h4>Klasse: {item['class']}</h4>\n")
                                if item["docstring"]:
                                    f.write(f"<p>Docstring: {item['docstring']}</p>\n")
                                for method in item["methods"]:
                                    params_str = ", ".join(method["params"])
                                    f.write(
                                        f"<p>Methode: {method['method']}({params_str})</p>\n"
                                    )
                                    if method["docstring"]:
                                        f.write(
                                            f"<p>Docstring: {method['docstring']}</p>\n"
                                        )
                            elif "function" in item:
                                params_str = ", ".join(item["params"])
                                f.write(
                                    f"<h4>Funktion: {item['function']}({params_str})</h4>\n"
                                )
                                if item["docstring"]:
                                    f.write(f"<p>Docstring: {item['docstring']}</p>\n")
                        else:
                            f.write(f"<p>{item}</p>\n")
                else:
                    f.write("<p>Keine Dokumentation</p>\n")

            f.write("</body></html>")

    def save_overview_as_json(self, output_file):
        """
        Saves the overview of classes, methods, and functions as a minified JSON file.
        Files with no documentation will be indicated.

        Args:
            output_file (str): The path to the JSON file where the overview will be saved.

        Returns:
            None
        """
        # Bereite das reduzierte JSON vor (ohne unnötige Formatierungen)
        with open(output_file, "w") as f:
            # Speichere das JSON in einer komprimierten Form (ohne Zeilenumbrüche und Leerzeichen)
            json.dump(self.overview, f, separators=(",", ":"), ensure_ascii=False)
