#Filename: modules/output.py
"""
OutputManager class to handle saving of generated project overviews in Markdown and HTML formats.

Imports:
    - os: Provides access to operating system functionalities like file paths.
    - save_as_md (modules.save): Function to save the overview as a Markdown file.
    - save_as_html (modules.save): Function to save the overview as an HTML file.

Classes:
    - OutputManager: Manages the process of saving the project overview to the target directory.

Usage:
    output_manager = OutputManager(target_dir)
    output_manager.save_overview(overview)

Attributes:
    - target_dir (str): The directory where the output files should be saved.
    - md_output_file (str): The name of the output Markdown file (default: "docu.MD").
    - html_output_file (str): The name of the output HTML file (default: "docu.html").

Methods:
    - __init__(target_dir): Initializes the class with the target directory.
    - save_overview(overview): Saves the provided overview in both Markdown and HTML formats in the specified target directory.
"""

import os
from modules.save import save_as_md, save_as_html


class OutputManager:
    def __init__(self, target_dir):
        """
        Initializes the OutputManager with the target directory and default output file names.

        Args:
            target_dir (str): The directory where the output files will be saved.
        
        Attributes:
            target_dir (str): The base directory for saving output.
            md_output_file (str): Default filename for Markdown output (default: 'docu.MD').
            html_output_file (str): Default filename for HTML output (default: 'docu.html').
        """
        self.target_dir = target_dir
        self.md_output_file = "docu.MD"
        self.html_output_file = "docu.html"

    def save_overview(self, overview):
        """
        Saves the provided project overview in both Markdown and HTML formats in the target directory.

        The method ensures that a subdirectory called 'doc' is created within the target directory 
        if it doesn't already exist. It then saves the overview as Markdown and HTML using the 
        `save_as_md` and `save_as_html` functions.

        Args:
            overview (dict): The overview data to be saved.

        Returns:
            None

        Raises:
            OSError: If there's an error creating the target directory.
        """
        target_dir = os.path.join(self.target_dir, "doc")
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        md_output_file = os.path.join(target_dir, self.md_output_file)
        html_output_file = os.path.join(target_dir, self.html_output_file)

        # Speichere als Markdown
        save_as_md(overview, md_output_file)
        print(f"Die Markdown-Datei wurde in '{md_output_file}' gespeichert.")

        # Speichere als HTML
        save_as_html(overview, html_output_file)
        print(f"Die HTML-Datei wurde in '{html_output_file}' gespeichert.")

#EOF
