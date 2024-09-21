# Filename: modules/args.py

import sys


class ArgumentParser:
    def __init__(self):
        self.project_path = "./"
        self.target_dir = "./"
        self.output_format = "md"
        self.show_help = False
        self.output_plain = False

    def parse_arguments(self):
        """
        Liest die Argumente aus und setzt die entsprechenden Optionen.
        """
        if "-h" in sys.argv:
            self.show_help = True
        if "-p" in sys.argv:
            self.output_plain = True
        if "-z" in sys.argv:
            try:
                self.target_dir = sys.argv[sys.argv.index("-z") + 1]
            except IndexError:
                print("Fehler: Kein Zielverzeichnis angegeben.")
        return self

    def print_help(self):
        """
        Zeigt die Hilfe für das Programm an.
        """
        help_text = """
        Nutzung:
          python main.py [-p] [-h] [-z ZIELVERZEICHNIS]
        
        Optionen:
          -p    Ausgabe in menschenlesbarer Form auf der Konsole und als Markdown speichern.
          -h    Hilfe anzeigen und Ausgabe in HTML speichern.
          -z    Speichern der Ausgabe im angegebenen Zielverzeichnis. Die Dateien werden im Unterverzeichnis 'doc' erstellt.
        
        Beispielaufrufe:
          python main.py -p
          python main.py -h
          python main.py -p -z /Pfad/zum/Zielverzeichnis
        """
        print(help_text)


# EOF
