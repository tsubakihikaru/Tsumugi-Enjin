import tkinter as tk
from tkinter import scrolledtext
import subprocess
import os

# --- Configuration ---
# Path to your Ren'Py executable (Beginners would change this)
RENPY_PATH = "C:/renpy/renpy.exe" 
# Path to the game project folder in your GitHub repo
PROJECT_PATH = "./game_template"

def launch_renpy():
    """Tells Ren'Py to run the game folder."""
    print("Launching Ren'Py...")
    try:
        # This command runs Ren'Py and points it at your template folder
        subprocess.Popen([RENPY_PATH, PROJECT_PATH])
    except Exception as e:
        print(f"Error: Could not find Ren'Py at {RENPY_PATH}\n{e}")

# --- UI Setup ---
root = tk.Tk()
root.title("Beginner Engine Editor")
root.geometry("900x650")

# 1. Toolbar (The 'Play' Button)
toolbar = tk.Frame(root, bg="#eeeeee", bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

btn_run = tk.Button(toolbar, text="▶ Run Game", command=launch_renpy, 
                    bg="#d4f1d4", padx=10, font=("Arial", 10, "bold"))
btn_run.pack(side=tk.LEFT, padx=5, pady=5)

# 2. The Text Editor (The 'Code' Area)
editor = scrolledtext.ScrolledText(root, font=("Consolas", 12), undo=True)
editor.pack(expand=True, fill='both', padx=5, pady=5)
editor.insert(tk.INSERT, "# Start writing your story below!\n\nlabel start:\n    $ start_scene = True\n    'Hello World!'")

# 3. The Shell (The 'Output' Area)
shell = tk.Text(root, height=10, bg="#ffffff", fg="#666666", font=("Consolas", 10))
shell.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
shell.insert(tk.INSERT, ">>> Engine Ready. Press 'Run Game' to test.")

root.mainloop()
