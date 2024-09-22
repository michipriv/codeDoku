# Filename: modules/args.py
"""
ArgumentParser class to handle command line argument parsing.

Imports:
    - sys: Provides access to command line arguments.
    - help (modules.help): Imports the function to display the help message.

Classes:
    - ArgumentParser: Handles the parsing of arguments like project path and target directory.

Usage:
    arg_parser = ArgumentParser()
    args = arg_parser.parse_arguments()

Attributes:
    - target_dir (str): Path to the target directory (which is scanned), must be provided via -z.
"""

import sys
import os
from modules.help import print_help


class ArgumentParser:
    def __init__(self):
        """
        Initializes the ArgumentParser with default values for the target directory.

        Attributes:
            target_dir (str): Path to the directory that will be scanned (provided via -z).
        """
        self.target_dir = None  # Muss durch die Option -z gesetzt werden

    def parse_arguments(self):
        """
        Reads command line arguments and sets the appropriate options for the target directory.

        This method looks for the '-z' argument in the command line to specify the target directory.
        If '-h' is provided, the help message is displayed, and the program exits.

        Raises:
            IndexError: If the '-z' argument is provided but no target directory follows it.

        Returns:
            ArgumentParser: Returns the current instance with updated attributes.
        """
        prog_name = os.path.basename(sys.argv[0])  # Ermittelt den Programmnamen

        if "-h" in sys.argv:
            print(print_help(prog_name))  # Übergibt den Programmnamen an print_help
            sys.exit(0)  # Beende das Programm nach der Anzeige der Hilfe

        if "-z" in sys.argv:
            try:
                self.target_dir = sys.argv[sys.argv.index("-z") + 1]
                if not os.path.exists(self.target_dir):
                    print(
                        f"Fehler: Das Verzeichnis '{self.target_dir}' existiert nicht."
                    )
                    sys.exit(1)
            except IndexError:
                print("Fehler: Kein Zielverzeichnis angegeben.")
                sys.exit(1)
        else:
            print(
                "Fehler: Die Option '-z' muss angegeben werden, um das zu scannende Zielverzeichnis festzulegen."
            )
            sys.exit(1)

        return self
