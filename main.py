# Filename: main.py

from modules.generator import OverviewGenerator
from modules.file_list_saver import FileListSaver
from modules.overview_saver import OverviewSaver
from modules.args import ArgumentParser
import os


def create_doc_directory(target_dir):
    """
    Ensures the 'doc' directory exists in the target directory.

    Args:
        target_dir (str): The path to the target directory where 'doc' should be created.

    Returns:
        str: The path to the 'doc' directory.
    """
    if not os.path.isabs(target_dir):
        target_dir = os.path.abspath(target_dir)

    doc_dir = os.path.join(target_dir, "doc")

    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

    return doc_dir


def main():
    """
    Main function to handle project overview generation and output saving.

    This function does the following:
    1. Parses command line arguments to get the target directory.
    2. Generates the list of files and the project overview.
    3. Saves the list of files and the overview in the 'doc' subdirectory.

    Args:
        None

    Returns:
        None
    """
    # Initialisiere die ArgumentParser Klasse
    arg_parser = ArgumentParser()
    args = arg_parser.parse_arguments()

    # Erstelle das doc-Verzeichnis im Zielverzeichnis
    doc_dir = create_doc_directory(args.target_dir)

    # Generiere die Liste der Dateien und die Übersicht
    generator = OverviewGenerator(args.target_dir)
    file_list = generator.scan_directory()
    overview = generator.generate_overview(file_list)

    # Speichere die Liste der Dateien
    file_saver = FileListSaver(file_list)  # Nur file_list wird übergeben
    file_saver.save_file_list_as_md(f"{doc_dir}/file_list.md")
    file_saver.save_file_list_as_html(f"{doc_dir}/file_list.html")

    # Speichere die Übersicht der Klassen, Methoden und Funktionen
    overview_saver = OverviewSaver(
        overview, file_list, args, os.path.basename(__file__)
    )
    overview_saver.save_overview_as_md(f"{doc_dir}/overview.md")
    overview_saver.save_overview_as_html(f"{doc_dir}/overview.html")

    # Speichere die Übersicht als komprimiertes JSON für die KI
    overview_saver.save_overview_as_json(f"{doc_dir}/overview.json")


if __name__ == "__main__":
    main()

# EOF
