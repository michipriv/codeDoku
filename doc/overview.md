# Kommandozeilen-Hilfe


    Nutzung:
      python main.py [-p] [-h] [-z ZIELVERZEICHNIS]
    
    Optionen:
      -p    Generiert eine Projektübersicht (Klassen, Methoden, Docstrings) und speichert diese in Markdown und HTML.
      -h    Zeigt diese Hilfemeldung an und beendet das Programm.
      -z    Spezifiziert das Zielverzeichnis für die gespeicherten Dateien (Markdown und HTML). Standard ist das aktuelle Verzeichnis.
    
    Beispielaufrufe:
      python main.py -p
      python main.py -p -z /Pfad/zum/Zielverzeichnis
      python main.py -h
    
# Übersicht der gescannten Dateien

- ./main.py
- ./modules/args.py
- ./modules/file_list_saver.py
- ./modules/generator.py
- ./modules/help.py
- ./modules/output.py
- ./modules/overview.py
- ./modules/overview_saver.py
- ./modules/save.py

# Dokumentation der Dateien

# Datei: ./main.py
  ## Funktion: create_doc_directory(target_dir)
    Docstring: Ensures the 'doc' directory exists in the target directory.

Args:
    target_dir (str): The path to the target directory where 'doc' should be created.

Returns:
    str: The path to the 'doc' directory.
  ## Funktion: main()
    Docstring: Main function to handle project overview generation and output saving.

This function does the following:
1. Parses command line arguments to get the project path and target directory.
2. Generates the list of files and the project overview.
3. Saves the list of files and the overview in Markdown, HTML, and JSON formats.

Args:
    None

Returns:
    None
# Datei: ./modules/args.py
  ## Klasse: ArgumentParser
    ### Methode: __init__(self)
      Docstring: Initializes the ArgumentParser with default values for project path and target directory.

Attributes:
    project_path (str): Path to the project directory, defaults to './'.
    target_dir (str): Path to the output directory, defaults to './'.
    ### Methode: parse_arguments(self)
      Docstring: Reads command line arguments and sets the appropriate options for project and target paths.

This method looks for the '-z' argument in the command line to specify the target directory.
If '-h' is provided, the help message is displayed, and the program exits.

Raises:
    IndexError: If the '-z' argument is provided but no target directory follows it.

Returns:
    ArgumentParser: Returns the current instance with updated attributes.
  ## Funktion: __init__(self)
    Docstring: Initializes the ArgumentParser with default values for project path and target directory.

Attributes:
    project_path (str): Path to the project directory, defaults to './'.
    target_dir (str): Path to the output directory, defaults to './'.
  ## Funktion: parse_arguments(self)
    Docstring: Reads command line arguments and sets the appropriate options for project and target paths.

This method looks for the '-z' argument in the command line to specify the target directory.
If '-h' is provided, the help message is displayed, and the program exits.

Raises:
    IndexError: If the '-z' argument is provided but no target directory follows it.

Returns:
    ArgumentParser: Returns the current instance with updated attributes.
# Datei: ./modules/file_list_saver.py
  ## Klasse: FileListSaver
    ### Methode: __init__(self, file_list, args, prog_name)
      Docstring: Initializes the FileListSaver with the list of scanned Python files, command-line arguments, and program name.

Args:
    file_list (list): A list of all Python files that were scanned.
    args (ArgumentParser): Parsed command-line arguments (e.g., project_path, target_dir).
    prog_name (str): The name of the program being executed.
    ### Methode: save_file_list_as_md(self, output_file)
      Docstring: Saves the list of scanned Python files as a Markdown file.

Args:
    output_file (str): The path to the Markdown file where the file list will be saved.

Returns:
    None
    ### Methode: save_file_list_as_html(self, output_file)
      Docstring: Saves the list of scanned Python files as an HTML file.

Args:
    output_file (str): The path to the HTML file where the file list will be saved.

Returns:
    None
  ## Funktion: __init__(self, file_list, args, prog_name)
    Docstring: Initializes the FileListSaver with the list of scanned Python files, command-line arguments, and program name.

Args:
    file_list (list): A list of all Python files that were scanned.
    args (ArgumentParser): Parsed command-line arguments (e.g., project_path, target_dir).
    prog_name (str): The name of the program being executed.
  ## Funktion: save_file_list_as_md(self, output_file)
    Docstring: Saves the list of scanned Python files as a Markdown file.

Args:
    output_file (str): The path to the Markdown file where the file list will be saved.

Returns:
    None
  ## Funktion: save_file_list_as_html(self, output_file)
    Docstring: Saves the list of scanned Python files as an HTML file.

Args:
    output_file (str): The path to the HTML file where the file list will be saved.

Returns:
    None
# Datei: ./modules/generator.py
  ## Klasse: OverviewGenerator
    ### Methode: __init__(self, project_path)
      Docstring: Initializes the OverviewGenerator with the provided project path.

Args:
    project_path (str): The directory path where the project files are located.
    ### Methode: generate_overview(self, file_list)
      Docstring: Generates an overview of classes, methods, and functions from all Python files in the given project path.
Uses the provided file list to ensure all files are documented, even if they contain no classes or methods.

Args:
    file_list (list): The list of Python files to document.

Returns:
    dict: A dictionary where the keys are file paths and the values are lists of extracted class, method, and function information.
    ### Methode: scan_directory(self)
      Docstring: Scans the project directory for Python files.
This function traverses the given project directory and returns the paths of all Python files.
    ### Methode: _extract_classes_funcs(self, file_path)
      Docstring: Extracts classes, methods, parameters, and docstrings from a Python file.
Also extracts top-level functions outside of classes.

Args:
    file_path (str): The path to the Python file to be analyzed.

Returns:
    list: A list of dictionaries containing class and method information, or function information.
  ## Funktion: __init__(self, project_path)
    Docstring: Initializes the OverviewGenerator with the provided project path.

Args:
    project_path (str): The directory path where the project files are located.
  ## Funktion: generate_overview(self, file_list)
    Docstring: Generates an overview of classes, methods, and functions from all Python files in the given project path.
Uses the provided file list to ensure all files are documented, even if they contain no classes or methods.

Args:
    file_list (list): The list of Python files to document.

Returns:
    dict: A dictionary where the keys are file paths and the values are lists of extracted class, method, and function information.
  ## Funktion: scan_directory(self)
    Docstring: Scans the project directory for Python files.
This function traverses the given project directory and returns the paths of all Python files.
  ## Funktion: _extract_classes_funcs(self, file_path)
    Docstring: Extracts classes, methods, parameters, and docstrings from a Python file.
Also extracts top-level functions outside of classes.

Args:
    file_path (str): The path to the Python file to be analyzed.

Returns:
    list: A list of dictionaries containing class and method information, or function information.
# Datei: ./modules/help.py
  ## Funktion: print_help(prog_name)
    Docstring: Displays a help message describing the command-line options for the program.

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
# Datei: ./modules/output.py
  ## Klasse: OutputManager
    ### Methode: __init__(self, target_dir)
      Docstring: Initializes the OutputManager with the target directory and default output file names.

Args:
    target_dir (str): The directory where the output files will be saved.

Attributes:
    target_dir (str): The base directory for saving output.
    md_output_file (str): Default filename for Markdown output (default: 'docu.MD').
    html_output_file (str): Default filename for HTML output (default: 'docu.html').
    ### Methode: save_overview(self, overview)
      Docstring: Saves the provided project overview in both Markdown and HTML formats in the target directory.

The method ensures that a subdirectory called 'doc' is created within the target directory 
if it doesn't already exist. It then saves the overview as Markdown and HTML using the 
`save_as_md` and `save_as_html` functions.

Args:
    overview (dict): The overview data to be saved.

Returns:
    None

Raises:
    OSError: If there's an error creating the target directory.
  ## Funktion: __init__(self, target_dir)
    Docstring: Initializes the OutputManager with the target directory and default output file names.

Args:
    target_dir (str): The directory where the output files will be saved.

Attributes:
    target_dir (str): The base directory for saving output.
    md_output_file (str): Default filename for Markdown output (default: 'docu.MD').
    html_output_file (str): Default filename for HTML output (default: 'docu.html').
  ## Funktion: save_overview(self, overview)
    Docstring: Saves the provided project overview in both Markdown and HTML formats in the target directory.

The method ensures that a subdirectory called 'doc' is created within the target directory 
if it doesn't already exist. It then saves the overview as Markdown and HTML using the 
`save_as_md` and `save_as_html` functions.

Args:
    overview (dict): The overview data to be saved.

Returns:
    None

Raises:
    OSError: If there's an error creating the target directory.
# Datei: ./modules/overview.py
  ## Funktion: extract_classes_funcs(file_path)
    Docstring: Extracts classes, methods, parameters, and docstrings from a Python file.

This function parses a Python file, extracting class and method definitions,
along with their parameters and docstrings.

Args:
    file_path (str): The path to the Python file to be analyzed.

Returns:
    list: A list of dictionaries, each containing:
        - 'class': Name of the class.
        - 'docstring': The class docstring.
        - 'methods': A list of dictionaries, each containing:
            - 'method': Method name.
            - 'params': List of method parameters.
            - 'docstring': The method's docstring.
  ## Funktion: scan_directory(path)
    Docstring: Scans the directory for Python files.

This function traverses the given directory and returns the paths of all Python files.

Args:
    path (str): The directory path to scan.

Returns:
    list: A list of file paths pointing to Python files.
  ## Funktion: generate_overview(path)
    Docstring: Generates an overview of classes, methods, parameters, and docstrings per Python file in the directory.

This function scans the specified directory, extracts information about classes and methods from each Python file,
and returns a structured overview.

Args:
    path (str): The directory path to scan for Python files.

Returns:
    dict: A dictionary where the keys are file paths and the values are lists of extracted class and method information.
# Datei: ./modules/overview_saver.py
  ## Klasse: OverviewSaver
    ### Methode: __init__(self, overview, file_list, args, prog_name)
      Docstring: Initializes the OverviewSaver with the project overview data, the list of all files, and program name.

Args:
    overview (dict): The overview of classes, methods, and functions. Each key is a file path, and the value is a list of class and function information.
    file_list (list): The list of all Python files to ensure all are documented.
    args (ArgumentParser): Parsed command-line arguments (e.g., project_path, target_dir).
    prog_name (str): The name of the program being executed.
    ### Methode: save_overview_as_md(self, output_file)
      Docstring: Saves the overview of classes, methods, and functions as a Markdown file.
Files with no documentation will be indicated.

Args:
    output_file (str): The path to the Markdown file where the overview will be saved.

Returns:
    None
    ### Methode: save_overview_as_html(self, output_file)
      Docstring: Saves the overview of classes, methods, and functions as an HTML file.
Files with no documentation will be indicated.

Args:
    output_file (str): The path to the HTML file where the overview will be saved.

Returns:
    None
    ### Methode: save_overview_as_json(self, output_file)
      Docstring: Saves the overview of classes, methods, and functions as a minified JSON file.
Files with no documentation will be indicated.

Args:
    output_file (str): The path to the JSON file where the overview will be saved.

Returns:
    None
  ## Funktion: __init__(self, overview, file_list, args, prog_name)
    Docstring: Initializes the OverviewSaver with the project overview data, the list of all files, and program name.

Args:
    overview (dict): The overview of classes, methods, and functions. Each key is a file path, and the value is a list of class and function information.
    file_list (list): The list of all Python files to ensure all are documented.
    args (ArgumentParser): Parsed command-line arguments (e.g., project_path, target_dir).
    prog_name (str): The name of the program being executed.
  ## Funktion: save_overview_as_md(self, output_file)
    Docstring: Saves the overview of classes, methods, and functions as a Markdown file.
Files with no documentation will be indicated.

Args:
    output_file (str): The path to the Markdown file where the overview will be saved.

Returns:
    None
  ## Funktion: save_overview_as_html(self, output_file)
    Docstring: Saves the overview of classes, methods, and functions as an HTML file.
Files with no documentation will be indicated.

Args:
    output_file (str): The path to the HTML file where the overview will be saved.

Returns:
    None
  ## Funktion: save_overview_as_json(self, output_file)
    Docstring: Saves the overview of classes, methods, and functions as a minified JSON file.
Files with no documentation will be indicated.

Args:
    output_file (str): The path to the JSON file where the overview will be saved.

Returns:
    None
# Datei: ./modules/save.py
  ## Funktion: save_as_md(overview, output_file)
    Docstring: Saves the overview as a human-readable Markdown file.

This function formats the overview of classes, methods, parameters, and docstrings 
and writes it to a Markdown file. The file contains hierarchical headers for files, classes, and methods.

Args:
    overview (dict): The overview of classes, methods, and parameters. Each key is a file path, and the value is a list of class information.
    output_file (str): The path to the Markdown file where the overview will be saved.

Returns:
    None
  ## Funktion: save_as_html(overview, output_file)
    Docstring: Saves the overview as an HTML file.

This function formats the overview of classes, methods, parameters, and docstrings 
and writes it to an HTML file. The output is structured with headers for files, classes, and methods.

Args:
    overview (dict): The overview of classes, methods, and parameters. Each key is a file path, and the value is a list of class information.
    output_file (str): The path to the HTML file where the overview will be saved.

Returns:
    None
