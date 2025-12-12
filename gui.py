import streamlit as st
import os
import json
import shutil
import time
from datetime import datetime

# ============================================================
#                 NOTES MANAGER CLASS
# ============================================================

class NotesManager:
    def __init__(self, path="data/notes.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.path, "r") as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        with open(self.path, "w") as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self, title, content):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes.append(note)
        self.save_notes()
        return note

    def get_note_by_id(self, nid):
        return next((n for n in self.notes if n["id"] == nid), None)

    def edit_note(self, nid, title=None, content=None):
        note = self.get_note_by_id(nid)
        if not note:
            return False
        if title:
            note["title"] = title
        if content:
            note["content"] = content
        note["modified"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_notes()
        return True

    def delete_note(self, nid):
        original_len = len(self.notes)
        self.notes = [n for n in self.notes if n["id"] != nid]
        self.save_notes()
        return len(self.notes) != original_len

    def search_notes(self, query):
        return [n for n in self.notes if query.lower() in n["title"].lower()]


# ============================================================
#                        CALCULATOR
# ============================================================

def calculator():
    st.header("🧮 Calculator")

    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)
    operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = "Error: Cannot divide by zero" if num2 == 0 else num1 / num2

        st.success(f"Result: {result}")


# ============================================================
#                        TIMER
# ============================================================

def timer_tool():
    st.header("⏳ Timer / Stopwatch")

    duration = st.number_input("Enter duration (seconds):", min_value=1)

    if st.button("Start Timer"):
        st.write("Running...")
        progress = st.progress(0)

        for i in range(duration):
            time.sleep(1)
            progress.progress((i + 1) / duration)

        st.success("⏰ Time’s up!")


# ============================================================
#                 FILE ORGANIZER
# ============================================================

def file_organizer():
    st.header("📁 File Organizer")

    folder = st.text_input("Enter folder path to organize:")

    if st.button("Organize Files"):
        if not os.path.isdir(folder):
            st.error("Folder does not exist.")
            return

        extensions = {
            "Images": [".jpg", ".png", ".jpeg"],
            "Documents": [".txt", ".pdf", ".docx"],
            "Audio": [".mp3", ".wav"],
            "Videos": [".mp4", ".mkv"],
            "Archives": [".zip", ".rar"]
        }

        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1]

                for folder_name, exts in extensions.items():
                    if ext.lower() in exts:
                        target_dir = os.path.join(folder, folder_name)
                        os.makedirs(target_dir, exist_ok=True)
                        shutil.move(file_path, os.path.join(target_dir, file))

        st.success("Files organized successfully!")


# ============================================================
#               BACKUP & RESTORE
# ============================================================

def backup_restore():
    st.header("🔄 Backup & Restore")

    backup_dir = "data/backups"
    os.makedirs(backup_dir, exist_ok=True)

    if st.button("Create Backup"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        shutil.copy("data/notes.json", f"{backup_dir}/notes_{timestamp}.json")
        st.success(f"Backup created: notes_{timestamp}.json")

    st.write("Available backups:")

    backups = os.listdir(backup_dir)
    selected_backup = st.selectbox("Select backup to restore:", backups)

    if st.button("Restore Backup"):
        shutil.copy(f"{backup_dir}/{selected_backup}", "data/notes.json")
        st.success("Backup restored successfully!")


# ============================================================
#                     NOTES MANAGER GUI
# ============================================================

def notes_manager_gui():
    nm = NotesManager()
    st.header("📝 Notes Manager")

    menu = st.selectbox("Choose an action:", [
        "View Notes", "Add Note", "Search Notes", "Edit Note", "Delete Note", "Export Notes"
    ])

    if menu == "View Notes":
        for note in nm.notes:
            st.subheader(f"{note['id']}. {note['title']}")
            st.write(note["content"])
            st.caption(f"Created: {note['created']} | Modified: {note['modified']}")
            st.markdown("---")

    elif menu == "Add Note":
        title = st.text_input("Title")
        content = st.text_area("Content")

        if st.button("Save Note"):
            if title.strip() == "" or content.strip() == "":
                st.error("Both title and content required.")
            else:
                nm.add_note(title, content)
                st.success("Note added successfully!")

    elif menu == "Search Notes":
        query = st.text_input("Search by title")
        if query:
            results = nm.search_notes(query)
            if not results:
                st.warning("No results found.")
            else:
                for n in results:
                    st.write(f"**{n['id']}. {n['title']}** - {n['modified']}")

    elif menu == "Edit Note":
        note_id = st.number_input("Enter Note ID", min_value=1, step=1)

        note = nm.get_note_by_id(int(note_id))
        if note:
            new_title = st.text_input("New Title", value=note["title"])
            new_content = st.text_area("New Content", value=note["content"])

            if st.button("Update Note"):
                nm.edit_note(int(note_id), title=new_title, content=new_content)
                st.success("Note updated!")
        else:
            st.error("Note not found.")

    elif menu == "Delete Note":
        note_id = st.number_input("Enter Note ID to delete", min_value=1, step=1)
        if st.button("Delete"):
            if nm.delete_note(int(note_id)):
                st.success("Deleted successfully.")
            else:
                st.error("Note not found.")

    elif menu == "Export Notes":
        export_path = "export/notes.txt"
        os.makedirs("export", exist_ok=True)

        with open(export_path, "w") as f:
            for note in nm.notes:
                f.write(f"{note['id']}. {note['title']}\n{note['content']}\n\n")

        st.success(f"Notes exported successfully: {export_path}")


# ============================================================
#                    STREAMLIT MAIN UI
# ============================================================

def main():
    st.title("🚀 Personal Productivity Suite (Streamlit GUI Version)")

    choice = st.sidebar.selectbox(
        "Select Tool",
        ["Home", "Notes Manager", "Calculator", "Timer", "File Organizer", "Backup & Restore"]
    )

    if choice == "Home":
        st.write("""
        ### Welcome to the Productivity Suite
        Select a tool from the menu on the left.
        """)

    elif choice == "Notes Manager":
        notes_manager_gui()

    elif choice == "Calculator":
        calculator()

    elif choice == "Timer":
        timer_tool()

    elif choice == "File Organizer":
        file_organizer()

    elif choice == "Backup & Restore":
        backup_restore()


if __name__ == "__main__":
    main()
