# Filename: modules/overview_saver.py

import json  # Importiere json für die JSON-Ausgabe
from modules.help import print_help


class OverviewSaver:
    def __init__(self, overview, file_list, args, prog_name):
        """
        Initializes the OverviewSaver with the project overview data, the list of all files, and program name.

        Args:
            overview (dict): The overview of classes, methods, and functions. Each key is a file path, and the value is a list of class and function information.
            file_list (list): The list of all Python files to ensure all are documented.
            args (ArgumentParser): Parsed command-line arguments (e.g., target_dir).
            prog_name (str): The name of the program being executed.
        """
        self.overview = overview
        self.file_list = file_list
        self.args = args
        self.prog_name = prog_name

    def extract_command_line_help(self, docstring):
        """
        Extracts the command line help from a given docstring.

        If the word 'Kommandozeilen' is found in the docstring, the entire docstring is used as command line help.

        Args:
            docstring (str): The docstring to search for command line options.

        Returns:
            str: The command line help or an empty string if not found.
        """
        if docstring and "Kommandozeilen" in docstring:
            return docstring
        return ""

    def save_overview_as_md(self, output_file):
        """
        Saves the overview of classes, methods, and functions as a Markdown file.
        The extracted command line help is added at the top if found.

        Args:
            output_file (str): The path to the Markdown file where the overview will be saved.

        Returns:
            None
        """
        with open(output_file, "w") as f:
            # Schreibe die Kommandozeilen-Hilfe an den Anfang, falls vorhanden
            command_line_help = self.get_overall_command_line_help()
            if command_line_help:
                f.write("# Kommandozeilen-Hilfe\n\n")
                f.write(f"{command_line_help}\n\n")
            else:
                f.write("Keine Kommandozeilen gefunden\n\n")

            f.write("# Übersicht der gescannten Dateien\n\n")
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
                                    command_line_help = self.extract_command_line_help(
                                        item["docstring"]
                                    )
                                    f.write(
                                        f"    Kommandozeilen-Hilfe: {command_line_help}\n"
                                        if command_line_help
                                        else ""
                                    )
                                for method in item["methods"]:
                                    params_str = ", ".join(method["params"])
                                    f.write(
                                        f"    ### Methode: {method['method']}({params_str})\n"
                                    )
                                    if method["docstring"]:
                                        f.write(
                                            f"      Docstring: {method['docstring']}\n"
                                        )
                                        command_line_help = (
                                            self.extract_command_line_help(
                                                method["docstring"]
                                            )
                                        )
                                        f.write(
                                            f"      Kommandozeilen-Hilfe: {command_line_help}\n"
                                            if command_line_help
                                            else ""
                                        )
                            elif "function" in item:
                                params_str = ", ".join(item["params"])
                                f.write(
                                    f"  ## Funktion: {item['function']}({params_str})\n"
                                )
                                if item["docstring"]:
                                    f.write(f"    Docstring: {item['docstring']}\n")
                                    command_line_help = self.extract_command_line_help(
                                        item["docstring"]
                                    )
                                    f.write(
                                        f"    Kommandozeilen-Hilfe: {command_line_help}\n"
                                        if command_line_help
                                        else ""
                                    )
                        else:
                            f.write(f"  {item}\n")
                else:
                    f.write("  Keine Dokumentation\n\n")

    def save_overview_as_html(self, output_file):
        """
        Saves the overview of classes, methods, and functions as an HTML file.
        The extracted command line help is added at the top if found.

        Args:
            output_file (str): The path to the HTML file where the overview will be saved.

        Returns:
            None
        """
        with open(output_file, "w") as f:
            f.write("<html><body>\n")

            # Schreibe die Kommandozeilen-Hilfe an den Anfang, falls vorhanden
            command_line_help = self.get_overall_command_line_help()
            if command_line_help:
                f.write("<h1>Kommandozeilen-Hilfe</h1>\n")
                f.write(f"<pre>{command_line_help}</pre>\n")
            else:
                f.write("<p>Keine Kommandozeilen gefunden</p>\n")

            f.write("<h1>Übersicht der gescannten Dateien</h1>\n<ul>\n")
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
                                    command_line_help = self.extract_command_line_help(
                                        item["docstring"]
                                    )
                                    f.write(
                                        f"<p>Kommandozeilen-Hilfe: {command_line_help}</p>\n"
                                        if command_line_help
                                        else ""
                                    )
                                for method in item["methods"]:
                                    params_str = ", ".join(method["params"])
                                    f.write(
                                        f"<p>Methode: {method['method']}({params_str})</p>\n"
                                    )
                                    if method["docstring"]:
                                        f.write(
                                            f"<p>Docstring: {method['docstring']}</p>\n"
                                        )
                                        command_line_help = (
                                            self.extract_command_line_help(
                                                method["docstring"]
                                            )
                                        )
                                        f.write(
                                            f"<p>Kommandozeilen-Hilfe: {command_line_help}</p>\n"
                                            if command_line_help
                                            else ""
                                        )
                            elif "function" in item:
                                params_str = ", ".join(item["params"])
                                f.write(
                                    f"<h4>Funktion: {item['function']}({params_str})</h4>\n"
                                )
                                if item["docstring"]:
                                    f.write(f"<p>Docstring: {item['docstring']}</p>\n")
                                    command_line_help = self.extract_command_line_help(
                                        item["docstring"]
                                    )
                                    f.write(
                                        f"<p>Kommandozeilen-Hilfe: {command_line_help}</p>\n"
                                        if command_line_help
                                        else ""
                                    )
                        else:
                            f.write(f"<p>{item}</p>\n")
                else:
                    f.write("<p>Keine Dokumentation</p>\n")

            f.write("</body></html>")

    def save_overview_as_json(self, output_file):
        """
        Saves the overview of classes, methods, and functions as a minified JSON file.
        Files with no documentation will be indicated. The command line help is included at the top if found.

        Args:
            output_file (str): The path to the JSON file where the overview will be saved.

        Returns:
            None
        """
        # Bereite das JSON-Objekt vor, das auch die Kommandozeilenparameter enthält
        output_data = {
            "command_line_help": self.get_overall_command_line_help(),
            "command_line_arguments": {
                "target_dir": self.args.target_dir,
            },
            "overview": self.overview,
        }

        # Speichere das JSON in einer komprimierten Form
        with open(output_file, "w") as f:
            json.dump(output_data, f, separators=(",", ":"), ensure_ascii=False)

    def get_overall_command_line_help(self):
        """
        Aggregates the command line help from all relevant docstrings in the overview.

        Returns:
            str: Aggregated command line help from all classes and functions or an empty string if not found.
        """
        command_line_help = ""
        for file_path in self.file_list:
            if file_path in self.overview and self.overview[file_path]:
                for item in self.overview[file_path]:
                    if isinstance(item, dict):
                        if "docstring" in item:
                            # Prüfe, ob die Klasse oder Funktion das Stichwort 'Kommandozeilen' enthält
                            help_text = self.extract_command_line_help(
                                item["docstring"]
                            )
                            if help_text:
                                command_line_help += help_text + "\n"
                        if "methods" in item:
                            for method in item["methods"]:
                                help_text = self.extract_command_line_help(
                                    method["docstring"]
                                )
                                if help_text:
                                    command_line_help += help_text + "\n"
        return command_line_help.strip()


# EOF
