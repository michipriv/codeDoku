# Filename: main.py

from modules.generator import OverviewGenerator
from modules.output import OutputManager
from modules.args import ArgumentParser


def main():
    # Initialisiere die ArgumentParser Klasse
    arg_parser = ArgumentParser()
    args = arg_parser.parse_arguments()

    # Initialisiere die Klassen für die Logik
    generator = OverviewGenerator(args.project_path)
    output_manager = OutputManager(args.target_dir)

    # Generiere die Übersicht
    overview = generator.generate_overview()

    if args.show_help:
        arg_parser.print_help()
    elif args.output_plain:
        output_manager.print_overview_plain(overview)
    else:
        output_manager.save_overview(overview, args.output_format)


if __name__ == "__main__":
    main()
# EOF
