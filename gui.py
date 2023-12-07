import tkinter as tk
import main

def on_commit():
    commit_window = tk.Toplevel(root)
    commit_window.title("Commit Changes")
    commit_window.minsize(300, 150)  # Set a minimum window size for the commit window

    # Function to close the commit window
    def close_commit_window():
        commit_window.destroy()

    # Title for the commit window
    title_label = tk.Label(commit_window, text="Commit Changes", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Subheading for the commit window
    subheading_label = tk.Label(commit_window, text="Enter Commit Message", font=("Arial", 12))
    subheading_label.pack(pady=5)

    # Textbox to enter commit message
    commit_text_entry = tk.Entry(commit_window, width=30)
    commit_text_entry.pack(pady=5)

    # Commit and Cancel buttons
    button_frame = tk.Frame(commit_window)
    button_frame.pack(pady=10)

    commit_button = tk.Button(button_frame, text="Commit", command=close_commit_window, width=10, height=1)
    commit_button.pack(side=tk.LEFT, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", command=close_commit_window, width=10, height=1)
    cancel_button.pack(side=tk.LEFT, padx=5)

def on_add():
    add_window = tk.Toplevel(root)
    add_window.title("Add new file")
    add_window.minsize(300, 150)  # Set a minimum window size for the commit window

    # Function to close the commit window
    def close_add_window():
        add_window.destroy()

    # Title for the commit window
    title_label = tk.Label(add_window, text="Add Files", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Subheading for the commit window
    subheading_label = tk.Label(add_window, text="Enter File name to be tracked", font=("Arial", 12))
    subheading_label.pack(pady=5)

    # Textbox to enter commit message
    add_text_entry = tk.Entry(add_window, width=30)
    add_text_entry.pack(pady=5)

    # Commit and Cancel buttons
    button_frame = tk.Frame(add_window)
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add", command=close_add_window, width=10, height=1)
    add_button.pack(side=tk.LEFT, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", command=close_add_window, width=10, height=1)
    cancel_button.pack(side=tk.LEFT, padx=5)

def on_logs():
    print("Logs button clicked")
    # Add your 'Logs' button logic here

def on_rollback():
    rb_window = tk.Toplevel(root)
    rb_window.title("Rollback")
    rb_window.minsize(300, 150)  # Set a minimum window size for the commit window

    # Function to close the commit window
    def close_rb_window():
        rb_window.destroy()

    # Title for the commit window
    title_label = tk.Label(rb_window, text="Rollback to previous version", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Subheading for the commit window
    subheading_label = tk.Label(rb_window, text="Enter commit ID to rollback to (include the #)", font=("Arial", 12))
    subheading_label.pack(pady=5)

    # Textbox to enter commit message
    rb_text_entry = tk.Entry(rb_window, width=30)
    rb_text_entry.pack(pady=5)

    # Commit and Cancel buttons
    button_frame = tk.Frame(rb_window)
    button_frame.pack(pady=10)

    rb_button = tk.Button(button_frame, text="Rollback", command=close_rb_window, width=10, height=1)
    rb_button.pack(side=tk.LEFT, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", command=close_rb_window, width=10, height=1)
    cancel_button.pack(side=tk.LEFT, padx=5)

def on_init():
    init_window = tk.Toplevel(root)
    init_window.title("Initialize Repo")
    init_window.minsize(300, 150)  # Set a minimum window size for the init window

    def get_info():
        pathInfo = init_text_entry.get()
        print(pathInfo)
        #main.mainfunc(pathInfo, "init")
        close_init_window()

    # Function to close the init window
    def close_init_window():
        init_window.destroy()

    # Title for the init window
    title_label = tk.Label(init_window, text="Initialize Repository", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Subheading for the init window
    subheading_label = tk.Label(init_window, text="Enter Path for File", font=("Arial", 12))
    subheading_label.pack(pady=5)

    # Textbox to enter init message
    init_text_entry = tk.Entry(init_window, width=30)
    init_text_entry.pack(pady=5)

    # Commit and Cancel buttons
    button_frame = tk.Frame(init_window)
    button_frame.pack(pady=10)

    init_button = tk.Button(button_frame, text="Initialize", command=close_init_window, width=10, height=1)
    init_button.pack(side=tk.LEFT, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", command=close_init_window, width=10, height=1)
    cancel_button.pack(side=tk.LEFT, padx=5)

def on_use_current_path():
    print("Use current path button clicked")
    
    # Add your 'Use current path' button logic here

def getPath():
    pathInfo = on_init.init_text_entry.get()
    print(pathInfo)
    on_init.close_init_window()


# Create the main application window
root = tk.Tk()
root.title("Version Control System")
root.minsize(500, 300)  # Set a minimum window size

# Add a big title and subtitle
title_label = tk.Label(root, text="Version Control System", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

subtitle_label = tk.Label(root, text="A python script for tracking changes made to files", font=("Arial", 14))
subtitle_label.pack(pady=10)

# Create a frame to hold the buttons and center it
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create and place the buttons
init_button = tk.Button(button_frame, text="Init", command=on_init, width=15, height=2)
init_button.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(button_frame, text="Add", command=on_add, width=15, height=2)
add_button.pack(side=tk.LEFT, padx=10)

commit_button = tk.Button(button_frame, text="Commit", command=on_commit, width=15, height=2)
commit_button.pack(side=tk.LEFT, padx=10)

logs_button = tk.Button(button_frame, text="Logs", command=on_logs, width=15, height=2)
logs_button.pack(side=tk.LEFT, padx=10)

rollback_button = tk.Button(button_frame, text="Rollback", command=on_rollback, width=15, height=2)
rollback_button.pack(side=tk.LEFT, padx=10)

# Add the 'Use current path' button with padding and button size
use_current_path_button = tk.Button(root, text="Use current path", command=on_use_current_path, width=20, height=2)
use_current_path_button.pack(pady=10)

root.mainloop()
