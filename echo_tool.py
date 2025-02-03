import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import json

class EchoTool:
    def __init__(self, root):
        self.root = root
        self.root.title("EchoTool")
        self.notes = {}
        self.load_notes()

        self.create_widgets()
        self.update_notes_display()

    def create_widgets(self):
        self.add_button = tk.Button(self.root, text="Add Note", command=self.add_note)
        self.add_button.pack(pady=5)

        self.notes_frame = tk.Frame(self.root)
        self.notes_frame.pack(fill=tk.BOTH, expand=True)

    def add_note(self):
        note_text = simpledialog.askstring("Input", "Enter your note:")
        if note_text:
            note_id = len(self.notes) + 1
            self.notes[note_id] = note_text
            self.save_notes()
            self.update_notes_display()

    def delete_note(self, note_id):
        if messagebox.askyesno("Delete", "Are you sure you want to delete this note?"):
            del self.notes[note_id]
            self.save_notes()
            self.update_notes_display()

    def update_notes_display(self):
        for widget in self.notes_frame.winfo_children():
            widget.destroy()

        for note_id, note_text in self.notes.items():
            note_frame = tk.Frame(self.notes_frame, bd=1, relief=tk.SOLID)
            note_frame.pack(fill=tk.X, pady=2, padx=5)

            note_label = tk.Label(note_frame, text=note_text, anchor='w')
            note_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

            delete_button = tk.Button(note_frame, text="Delete", command=lambda nid=note_id: self.delete_note(nid))
            delete_button.pack(side=tk.RIGHT)

    def save_notes(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as f:
                self.notes = json.load(f)

def main():
    root = tk.Tk()
    app = EchoTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()