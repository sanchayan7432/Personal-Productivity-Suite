"""Notes manager with JSON persistence and basic operations."""
from .utils import NOTES_FILE, safe_input, timestamp_now
import json
from pathlib import Path

class NotesManager:
    def __init__(self):
        self.notes_file = Path(NOTES_FILE)
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with self.notes_file.open('r', encoding='utf-8') as f:
                self.notes = json.load(f)
        except Exception:
            self.notes = []

    def save_notes(self):
        with self.notes_file.open('w', encoding='utf-8') as f:
            json.dump(self.notes, f, indent=2, ensure_ascii=False)

    def add_note(self, title: str, content: str):
        note = {
        'id': (self.notes[-1]['id'] + 1) if self.notes else 1,
        'title': title,
        'content': content,
        'created': timestamp_now(),
        'modified': timestamp_now()
        }
        self.notes.append(note)
        self.save_notes()
        return note
    
    def list_notes(self):
        return list(self.notes)

    def find_notes(self, query: str):
        q = query.lower()
        return [n for n in self.notes if q in n['title'].lower() or q in n['content'].lower()]

    def get_note_by_id(self, note_id: int):
        for n in self.notes:
            if n['id'] == note_id:
                return n
        return None

    def edit_note(self, note_id: int, title: str = None, content: str = None):
        note = self.get_note_by_id(note_id)
        if not note:
            return None
        if title:
            note['title'] = title
        if content:
            note['content'] = content
        note['modified'] = timestamp_now()
        self.save_notes()
        return note
    
    def delete_note(self, note_id: int):
        before = len(self.notes)
        self.notes = [n for n in self.notes if n['id'] != note_id]
        if len(self.notes) < before:
            self.save_notes()
            return True
        return False

    def export_notes_txt(self, path: str):
        with open(path, 'w', encoding='utf-8') as f:
            for n in self.notes:
                f.write(f"ID: {n['id']}\nTitle: {n['title']}\nCreated: {n['created']}\nModified: {n['modified']}\nContent:\n{n['content']}\n\n---\n\n")

def run():
    nm = NotesManager()
    MENU = '''\nNOTES MANAGER:\n1. View All Notes\n2. Add New Note\n3. Search Notes\n4. Edit Note\n5. Delete Note\n6. Export Notes\n7. Back to Main Menu\n'''
    while True:
        print(MENU)
        choice = safe_input('Enter choice: ').strip()
        if choice == '1':
            notes = nm.list_notes()
            if not notes:
                print('No notes found.')
            else:
                for n in notes:
                    print(f"ID: {n['id']} | Title: {n['title']} | Created: {n['created']}")
                safe_input('\nPress Enter to continue...')
        elif choice == '2':
            title = safe_input('Enter note title: ').strip()
            content_lines = []
            print('Enter note content. Finish with a single line containing only "."')
            while True:
                line = safe_input('')
                if line.strip() == '.':
                    break
                content_lines.append(line)
            content = '\n'.join(content_lines)
            note = nm.add_note(title, content)
            print('\n✅ Note added successfully!')
            print(f"Note ID: {note['id']}\nCreated: {note['created']}")
        elif choice == '3':
            q = safe_input('Search query: ').strip()
            results = nm.find_notes(q)
            if not results:
                print('No matches.')
            else:
                for n in results:
                    print(f"ID: {n['id']} | Title: {n['title']} | Modified: {n['modified']}")
        elif choice == '4':
            id_str = safe_input('Enter note ID to edit: ').strip()
            if not id_str.isdigit():
                print('Invalid ID.')
                continue
            nid = int(id_str)
            note = nm.get_note_by_id(nid)
            if not note:
                print('Note not found.')
                continue
            title = safe_input(f"New title (leave blank to keep) [{note['title']}]: ") or None
            print('Enter new content. Finish with a single line containing only "." (leave blank to keep)')
            content_lines = []
            while True:
                line = safe_input('')
                if line.strip() == '.':
                    break
                content_lines.append(line)
            content = '\n'.join(content_lines) if content_lines else None
            updated = nm.edit_note(nid, title=title or None, content=content)
            if updated:
                print('Note updated.')
            else:
                print('Failed to update.')
        elif choice == '5':
            id_str = safe_input('Enter note ID to delete: ').strip()
            if not id_str.isdigit():
                print('Invalid ID.')
                continue
            success = nm.delete_note(int(id_str))
            print('Deleted.' if success else 'Note not found.')
        elif choice == '6':
            path = safe_input('Export path (e.g. export/notes.txt): ').strip()
            if not path:
                print('Invalid path.')
                continue
            try:
                nm.export_notes_txt(path)
                print('Exported to', path)
            except Exception as e:
                print('Export failed:', e)
        elif choice == '7' or choice == '':
            break
        else:
            print('Invalid choice')