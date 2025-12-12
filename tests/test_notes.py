import tempfile
from modules.notes_manager import NotesManager


def test_add_and_get_note():
    nm = NotesManager()

    # Isolate by setting notes_file to a temp file
    nm.notes_file = nm.notes_file.parent / 'test_notes.json'
    if nm.notes_file.exists():
        nm.notes_file.unlink()

    nm.load_notes()

    note = nm.add_note('Test', 'Content')
    assert note['title'] == 'Test'

    got = nm.get_note_by_id(note['id'])
    assert got is not None

    nm.notes_file.unlink()
