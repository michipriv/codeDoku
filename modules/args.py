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
    - project_path (str): Path to the project directory, default is './'.
    - target_dir (str): Path to the target directory for output, default is './'.

Methods:
    - __init__(): Initializes the class with default project and target directory.
    - parse_arguments(): Reads and processes command line arguments to set options.
"""

import sys
from modules.help import print_help


class ArgumentParser:
    def __init__(self):
        """
        Initializes the ArgumentParser with default values for project path and target directory.

        Attributes:
            project_path (str): Path to the project directory, defaults to './'.
            target_dir (str): Path to the output directory, defaults to './'.
        """
        self.project_path = "./"
        self.target_dir = "./"

    def parse_arguments(self):
        """
        Reads command line arguments and sets the appropriate options for project and target paths.

        This method looks for the '-z' argument in the command line to specify the target directory.
        If '-h' is provided, the help message is displayed, and the program exits.

        Raises:
            IndexError: If the '-z' argument is provided but no target directory follows it.

        Returns:
            ArgumentParser: Returns the current instance with updated attributes.
        """
        if "-h" in sys.argv:
            print_help()
            sys.exit(0)  # Beende das Programm nach der Anzeige der Hilfe

        if "-z" in sys.argv:
            try:
                self.target_dir = sys.argv[sys.argv.index("-z") + 1]
            except IndexError:
                print("Fehler: Kein Zielverzeichnis angegeben.")
        return self


# EOF
