# Filename: modules/file_list_saver.py
"""
FileListSaver class to save the list of scanned Python files in Markdown and HTML formats.

Classes:
    - FileListSaver: Manages the process of saving the list of Python files.

Functions:
    - save_file_list_as_md(file_list, output_file): Saves the list of Python files as a Markdown file.
    - save_file_list_as_html(file_list, output_file): Saves the list of Python files as an HTML file.

Attributes:
    - file_list (list): The list of all scanned Python files.
    - args (ArgumentParser): The parsed command-line arguments to include in the output files.
    - prog_name (str): The name of the program being executed, used for dynamic help.
"""

from modules.help import print_help


class FileListSaver:
    def __init__(self, file_list, args, prog_name):
        """
        Initializes the FileListSaver with the list of scanned Python files, command-line arguments, and program name.

        Args:
            file_list (list): A list of all Python files that were scanned.
            args (ArgumentParser): Parsed command-line arguments (e.g., project_path, target_dir).
            prog_name (str): The name of the program being executed.
        """
        self.file_list = file_list
        self.args = args
        self.prog_name = prog_name

    def save_file_list_as_md(self, output_file):
        """
        Saves the list of scanned Python files as a Markdown file.

        Args:
            output_file (str): The path to the Markdown file where the file list will be saved.

        Returns:
            None
        """
        with open(output_file, "w") as f:
           

            f.write("# Übersicht der gescannten Dateien\n\n")
            for file in self.file_list:
                f.write(f"- {file}\n")

    def save_file_list_as_html(self, output_file):
        """
        Saves the list of scanned Python files as an HTML file.

        Args:
            output_file (str): The path to the HTML file where the file list will be saved.

        Returns:
            None
        """
        with open(output_file, "w") as f:
           

            f.write("<h1>Übersicht der gescannten Dateien</h1>\n<ul>\n")
            for file in self.file_list:
                f.write(f"<li>{file}</li>\n")
            f.write("</ul>\n</body></html>")


# EOF
