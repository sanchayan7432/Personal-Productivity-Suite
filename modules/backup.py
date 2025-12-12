"""Backup and restore for data files."""
from .utils import BACKUP_DIR, DATA_DIR, safe_input
from pathlib import Path
import shutil
import zipfile
import datetime


def make_backup():
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    target = Path(BACKUP_DIR) / f'backup_{ts}.zip'

    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in Path(DATA_DIR).iterdir():
            if f.is_file():
                zf.write(f, arcname=f.name)

    return target


def list_backups():
    return sorted(Path(BACKUP_DIR).glob('backup_*.zip'))


def restore_backup(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError('Backup not found')

    with zipfile.ZipFile(p, 'r') as zf:
        zf.extractall(Path(DATA_DIR))


def run():
    MENU = (
        "\nBACKUP & RESTORE:\n"
        "1. Create Backup\n"
        "2. List Backups\n"
        "3. Restore Backup\n"
        "4. Back to Main Menu\n"
    )

    while True:
        print(MENU)
        c = safe_input('Choice: ').strip()

        if c == '1':
            try:
                b = make_backup()
                print('Created backup at', b)
            except Exception as e:
                print('Backup failed:', e)

        elif c == '2':
            for b in list_backups():
                print(b.name)

        elif c == '3':
            p = safe_input('Backup filename (from list): ').strip()
            try:
                restore_backup(Path(BACKUP_DIR) / p)
                print('Restore completed')
            except Exception as e:
                print('Restore failed:', e)

        elif c == '4' or c == '':
            break

        else:
            print('Invalid choice')
