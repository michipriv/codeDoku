# Filename: modules/help.py


def print_help():
    """
    Zeigt die Hilfe an, die die Optionen für den Programmaufruf beschreibt.
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
