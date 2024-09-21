# Filename: modules/generator.py

from modules.overview import generate_overview


class OverviewGenerator:
    def __init__(self, project_path):
        self.project_path = project_path

    def generate_overview(self):
        """
        Generiert die Übersicht der Klassen und Methoden aus dem angegebenen Projektpfad.
        """
        return generate_overview(self.project_path)


# EOF
