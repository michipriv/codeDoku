# Filename: modules/help.py
"""
print_help function to display the help message for the program.

Functions:
    - print_help(prog_name): Displays a formatted help message that explains the usage and available options for the given program.

Usage:
    Call print_help() with the specific program name to display the help message.
"""


def print_help(prog_name):
    """
    Kommandozeilen
    Displays a help message describing the command-line options for the program.

    The message includes:
        - Program usage
        - Available options and their descriptions
        - Example command invocations

    The options explained include:
        - -p: Generates the project overview and saves it in both Markdown and HTML formats.
        - -h: Displays the help message and exits the program.
        - -z: Specifies the output directory for saving the generated files (Markdown and HTML).

    Args:
        prog_name (str): The name of the program for which the help is being generated.

    Example usage:
        - python {prog_name} -p
        - python {prog_name} -h
        - python {prog_name} -p -z /Path/to/TargetDirectory
    """
    help_text = f"""
    Nutzung:
      python {prog_name} [-p] [-h] [-z ZIELVERZEICHNIS]
    
    Optionen:
      -p    Generiert eine Projektübersicht (Klassen, Methoden, Docstrings) und speichert diese in Markdown und HTML.
      -h    Zeigt diese Hilfemeldung an und beendet das Programm.
      -z    Spezifiziert das Zielverzeichnis für die gespeicherten Dateien (Markdown und HTML). Standard ist das aktuelle Verzeichnis.
    
    Beispielaufrufe:
      python {prog_name} -p
      python {prog_name} -p -z /Pfad/zum/Zielverzeichnis
      python {prog_name} -h
    """
    return help_text


# EOF
