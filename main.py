import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import threading
from converter import convert

def scan_directory(directory_path):
    mp4_files = [file for file in os.listdir(directory_path) if file.endswith(".mp4")]
    return mp4_files
def select_all():
    listbox.select_set(0, tk.END)
def threaded_task(selected_files):
    failed=[]
    for i in len(range(selected_files)) :
        file=selected_files[i]
        task_status.set(f"converting {file}")
        try : convert(file[:-4])
        except : failed.append(file)
    start_button.config(state=tk.NORMAL)
    browse_button.config(state=tk.NORMAL)
    if len(failed)>0 :
        if len(failed) == len(selected_files) :
            messagebox.showerror("Error", "Failed to convert all files :(")
        else :
            messagebox.showerror("Error", "Failed to convert files :\n{}".format("\n".join(failed)))
    task_status.set(f"finished converting")

def start_threaded_task():
    selected_files = listbox.curselection()
    if not selected_files:
        messagebox.showerror("Error", "Please select at least one file.")
        return
    start_button.config(state=tk.DISABLED)
    browse_button.config(state=tk.DISABLED)
    selected_files = [listbox.get(index) for index in selected_files]

    thread = threading.Thread(target=threaded_task, args=(selected_files,))
    thread.start()

def select_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        listbox.delete(0, tk.END)
        mp4_files = scan_directory(directory_path)
        for file in mp4_files:
            listbox.insert(tk.END, file)

def auto_scan_current_directory():
    current_directory = os.getcwd()
    mp4_files = scan_directory(current_directory)
    for file in mp4_files:
        listbox.insert(tk.END, file)

root = tk.Tk()
root.title("MP4 File Scanner")
root.geometry("400x300")  # Set the window size

style = ttk.Style()
style.theme_use("clam")  # Use a different ttk theme for a modern appearance

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack(fill=tk.BOTH, expand=True)


# Add a "Select All" button
select_all_button = ttk.Button(root, text="Select All", command=select_all)
select_all_button.pack()

browse_button = ttk.Button(root, text="Browse", command=select_directory)
browse_button.pack()

start_button = ttk.Button(root, text="Convert to MP3", command=start_threaded_task)
start_button.pack()

task_status = tk.StringVar()
status_label = ttk.Label(root, textvariable=task_status)
status_label.pack()
auto_scan_current_directory()  # Automatically scan the current directory when the GUI starts

root.mainloop()
