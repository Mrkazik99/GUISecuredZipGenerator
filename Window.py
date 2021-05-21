import tkinter as tk
from tkinter import ttk
import Utils

password_file_types = [("Yaml", "*.yml"), ("Text File", "*.txt")]


def generate_window():
    window = tk.Tk()
    window.title("Secured Zip Generator")
    window.geometry("800x600")

    frm_passwords = tk.Frame(master=window)

    lbl_password = tk.Label(master=frm_passwords, text="Password file")
    lbl_password.pack()

    lbl_password_path = tk.Label(master=frm_passwords, text="")
    lbl_password_path.pack()

    btn_password = tk.Button(master=frm_passwords, text="Pick passwords file",
                             command=lambda: Utils.get_file_path(password_file_types, lbl_password_path))
    btn_password.pack()

    frm_source_dir = tk.Frame(master=window)

    lbl_source_dir = tk.Label(master=frm_source_dir, text="Source Directory")
    lbl_source_dir.pack()

    lbl_source_dir_path = tk.Label(master=frm_source_dir, text="")
    lbl_source_dir_path.pack()

    btn_source_dir = tk.Button(master=frm_source_dir, text="Pick source directory",
                               command=lambda: Utils.get_dir_path(lbl_source_dir_path))
    btn_source_dir.pack()

    frm_dest_dir = tk.Frame()

    lbl_dest_dir = tk.Label(master=frm_dest_dir, text="Destination Directory")
    lbl_dest_dir.pack()

    lbl_dest_dir_path = tk.Label(master=frm_dest_dir, text="")
    lbl_dest_dir_path.pack()

    btn_dest_dir = tk.Button(master=frm_dest_dir, text="Pick destination directory",
                             command=lambda: Utils.get_dir_path(lbl_dest_dir_path))
    btn_dest_dir.pack()

    frm_passwords.pack(pady=10)

    frm_submit_buttons = tk.Frame(master=window)

    btn_cancel = tk.Button(master=frm_submit_buttons, text="Cancel and Exit",
                           command=lambda: exit(0))
    btn_cancel.pack(side=tk.LEFT)

    btn_clear = tk.Button(master=frm_submit_buttons, text="Clear Form",
                          command=lambda: Utils.clear_form([lbl_dest_dir_path, lbl_source_dir_path, lbl_password_path]))
    btn_clear.pack(side=tk.LEFT)

    btn_submit = tk.Button(master=frm_submit_buttons, text="Start")
    btn_submit.pack(side=tk.LEFT)

    separator = ttk.Separator(master=window, orient='horizontal')
    separator.pack(fill='x')

    frm_source_dir.pack(pady=10)

    separator = ttk.Separator(master=window, orient='horizontal')
    separator.pack(fill='x')

    frm_dest_dir.pack(pady=10)

    separator = ttk.Separator(master=window, orient='horizontal')
    separator.pack(fill='x')

    frm_submit_buttons.pack(pady=10)

    window.mainloop()
