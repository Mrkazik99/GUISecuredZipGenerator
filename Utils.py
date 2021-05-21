from tkinter import filedialog
import tkinter as tk


def get_dir_path(output: tk.Label) -> None:
    output.config(text=filedialog.askdirectory())


def get_file_path(types: list, output: tk.Label) -> None:
    output.config(text=filedialog.askopenfilename(filetypes=types))


def clear_form(items: list) -> None:
    for element in items:
        element.config(text="")
