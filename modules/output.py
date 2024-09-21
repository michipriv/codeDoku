# Filename: modules/output.py

import os
from modules.save import save_as_md, save_as_html


class OutputManager:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.md_output_file = "docu.MD"
        self.html_output_file = "docu.html"

    def save_overview(self, overview, output_format):
        """
        Speichert die Übersicht im gewünschten Format (Markdown oder HTML).
        """
        target_dir = os.path.join(self.target_dir, "doc")
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        md_output_file = os.path.join(target_dir, self.md_output_file)
        html_output_file = os.path.join(target_dir, self.html_output_file)

        if output_format == "md":
            save_as_md(overview, md_output_file)
            print(f"Die Markdown-Datei wurde in '{md_output_file}' gespeichert.")
        else:
            save_as_html(overview, html_output_file)
            print(f"Die HTML-Datei wurde in '{html_output_file}' gespeichert.")

    def print_overview_plain(self, overview):
        """
        Gibt die Übersicht in menschenlesbarer Form auf der Konsole aus.
        """
        print("Ausgabe in menschenlesbarer Form:")
        for file_path, classes in overview.items():
            print(f"Datei: {file_path}")
            for cls in classes:
                print(f"  Klasse: {cls['class']}")
                if cls["docstring"]:
                    print(f"    Docstring: {cls['docstring']}")
                for method in cls["methods"]:
                    params_str = ", ".join(method["params"])
                    print(f"    Methode: {method['method']}({params_str})")
                    if method["docstring"]:
                        print(f"      Docstring: {method['docstring']}")
            print()


# EOF
