import tkinter as tk
from tkinter import scrolledtext
import subprocess
import os

# --- Configuration ---
RENPY_PATH = "C:/renpy/renpy.exe" 
# This points to the actual script file in your template
SCRIPT_PATH = "./project_template/game/script.rpy"
PROJECT_FOLDER = "./project_template"

def save_and_run():
    """Saves the editor text to script.rpy and launches the engine."""
    # 1. Get text from the editor
    content = editor.get("1.0", tk.END)
    
    # 2. Write/Overwrite the script.rpy file
    try:
        with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print("File Saved!")
    except Exception as e:
        shell.insert(tk.INSERT, f"\nError saving file: {e}")
        return

    # 3. Launch Ren'Py
    try:
        subprocess.Popen([RENPY_PATH, PROJECT_FOLDER])
    except Exception as e:
        shell.insert(tk.INSERT, f"\nError: Ren'Py not found at {RENPY_PATH}")

# --- UI Setup ---
root = tk.Tk()
root.title("Beginner Engine Editor")

# Load existing script.rpy content into the editor at startup
initial_text = ""
if os.path.exists(SCRIPT_PATH):
    with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
        initial_text = f.read()

# Toolbar
toolbar = tk.Frame(root, bg="#eeeeee")
toolbar.pack(side=tk.TOP, fill=tk.X)

btn_run = tk.Button(toolbar, text="▶ Save & Run", command=save_and_run, bg="#d4f1d4")
btn_run.pack(side=tk.LEFT, padx=5, pady=5)

# Editor Area
editor = scrolledtext.ScrolledText(root, font=("Consolas", 12))
editor.pack(expand=True, fill='both')
editor.insert(tk.INSERT, initial_text) # This puts the current rpy code in the window

# Shell
shell = tk.Text(root, height=5, bg="#f0f0f0")
shell.pack(side=tk.BOTTOM, fill=tk.X)
shell.insert(tk.INSERT, "System: Ready to code.")

root.mainloop()

