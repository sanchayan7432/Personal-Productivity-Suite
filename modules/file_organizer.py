"""Simple file organizer that groups files by extension into folders."""
from .utils import safe_input
from pathlib import Path
import shutil


def organize_folder(path: str):
    p = Path(path)
    if not p.exists() or not p.is_dir():
        raise FileNotFoundError('Path does not exist or is not a directory')

    for item in p.iterdir():
        if item.is_file():
            ext = item.suffix.lower().lstrip('.') or 'no_ext'
            target = p / ext
            target.mkdir(exist_ok=True)
            shutil.move(str(item), str(target / item.name))


def run():
    MENU = (
        "\nFILE ORGANIZER:\n"
        "1. Organize a Folder by Extension\n"
        "2. Preview Folder Contents\n"
        "3. Back to Main Menu\n"
    )

    while True:
        print(MENU)
        c = safe_input('Choice: ').strip()

        if c == '1':
            path = safe_input('Folder path to organize: ').strip()
            try:
                organize_folder(path)
                print('Organization complete.')
            except Exception as e:
                print('Error:', e)

        elif c == '2':
            path = safe_input('Folder path to preview: ').strip()
            p = Path(path)
            if not p.exists() or not p.is_dir():
                print('Invalid path')
            else:
                for f in p.iterdir():
                    print(f.name)

        elif c == '3' or c == '':
            break

        else:
            print('Invalid choice')
