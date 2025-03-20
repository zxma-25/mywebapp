import tkinter as tk
from tkinter import filedialog, messagebox
import os

class NotesApp:
     def __init__(self, root):
        self.root = root
        self.root.title("Notes")
        self.root.geometry("800x400")
        
        # Dark mode colors
        self.bg_color = "#2E2E2E"
        self.text_color = "#FFFFFF"
        self.accent_color = "#363434"
        
        # Configure root window
        self.root.configure(bg=self.bg_color)
        
        # Frame for text area
        self.text_frame = tk.Frame(self.root, bg=self.bg_color)
        self.text_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        # Create Text Widget
        self.text_area = tk.Text(self.text_frame, wrap="word", bg=self.bg_color, fg=self.text_color, insertbackground=self.text_color,
                                 font=("Open Sans", 12), padx=10, pady=10, undo=True)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        # Create Menu Bar
        self.menu_bar = tk.Menu(self.root, tearoff=0, bg=self.accent_color, fg=self.text_color)
        
        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.accent_color, fg=self.text_color)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        self.root.config(menu=self.menu_bar)

        #define file menu functions
        def new_file():
            global file
            root.title("Untitled - Notes")
            file = None
            textArea.delete(1.0, END)
        def open_file(self):
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if file_path:
                self.text_area.delete("1.0", tk.END)
                with open(file_path, "r") as file:
                    self.text_area.insert(tk.END, file.read())
                self.root.title(f"Notes - {os.path.basename(file_path)}")
        def save_file(self):
            file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get("1.0", tk.END))
                self.root.title(f"Notes - {os.path.basename(file_path)}")
        def exit(self):
            self.root.quit()

        #edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.accent_color, fg=self.text_color)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all)

        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        #define edit menu functions
        def cut_text(self):
            self.text_area.event_generate("<<Cut>>")
        def copy_text(self):
            self.text_area.event_generate("<<Copy>>")
        def paste_text(self):
            self.text_area.event_generate("<<Paste>>")
        def select_all(self):
            self.text_area.tag_add("sel", "1.0", tk.END)
            return "break"
        
        #help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.accent_color, fg=self.text_color)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        #define help menu functions
        def show_about(self):
            messagebox.showinfo("About", "Notes App created by Zama Mabaso.")



if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()