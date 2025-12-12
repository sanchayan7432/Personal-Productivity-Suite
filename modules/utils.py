"""Utility helpers for data directories, safe input and printing."""
import os
from pathlib import Path
import json


ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / 'data'
BACKUP_DIR = DATA_DIR / 'backups'
NOTES_FILE = DATA_DIR / 'notes.json'




def ensure_data_dirs():
    DATA_DIR.mkdir(exist_ok=True)
    BACKUP_DIR.mkdir(exist_ok=True)
    if not NOTES_FILE.exists():
        NOTES_FILE.write_text('[]', encoding='utf-8')




def safe_input(prompt: str) -> str:
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print('\nInput cancelled. Returning to menu.')
        return ''




def timestamp_now():
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')