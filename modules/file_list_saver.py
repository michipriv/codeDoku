# Filename: modules/file_list_saver.py


class FileListSaver:
    def __init__(self, file_list):
        """
        Initializes the FileListSaver with the list of scanned Python files.

        Args:
            file_list (list): A list of all Python files that were scanned.
        """
        self.file_list = file_list

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
            f.write("<html><body>\n")
            f.write("<h1>Übersicht der gescannten Dateien</h1>\n<ul>\n")
            for file in self.file_list:
                f.write(f"<li>{file}</li>\n")
            f.write("</ul>\n</body></html>")


# EOF
