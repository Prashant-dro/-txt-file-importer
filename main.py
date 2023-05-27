import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

class Importer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File importer")
        self.root.geometry("600x500")

        self.main_text = tk.Label(self.root, text="Files importer...", font=("calibri", 20))
        self.main_text.pack()

        # self.browse_text = tk.StringVar()
        self.browse_button = tk.Button(self.root, text="Browse", font=("calibri", 15), command=self.open_file)
        # self.browse_text.set("Browse")
        self.browse_button.pack()

        self.text = tk.Text(self.root, font=("calibri", 15, "bold"))
        self.text.pack(padx=10, pady=10)

        self.root.mainloop()


    def open_file(self):
        # browse_text.set("loading...")
        self.text.delete(1.0, tk.END)
    
        self.file_path = filedialog.askopenfilename(initialdir="C:/Users/dell/OneDrive/Desktop/Python Programs/Practice", title="Open Text file", filetypes=(("Text Files", "*.txt"),))
        self.file = open(self.file_path, 'r')
        self.content = self.file.read()
        self.text.insert(1.0, self.content)
        # browse_text.set("Browse")


if __name__ == "__main__":
    Importer()
