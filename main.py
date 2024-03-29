import commands
import os

#C:\Users\kunal\oof
import tkinter as tk


# x = r'{}'.format(input("Enter directory path: "))

# print(repo_dir)
# repo_dir = ""
# x="default"

# cmd = "default"
# path="default"
# repo_name="default"

def mf_1():
    repo_dir = path
    repo_name = repo_dir.split("/")[-1].replace(" ", "_")
    print(repo_name)
    e = False
    while not e:
        #command = input("$>").split(" ")

        if cmd == "init":
            print("INIT YAY")
            try:
                commands.init(repo_name, repo_dir)
                os.chdir(os.path.join(repo_dir, ".vcr"))
            except FileExistsError:
                print("This folder is already a repository")
        try:
            os.chdir(os.path.join(repo_dir, ".vcr"))
        
        except:
            pass

        if cmd == "add":
            files = []
            try:
                if command[1] == "*":
                    ignoreExt = input("Enter the file extensions you want to ignore (separated by a comma (,). \n For example, if you wish to ignore all .pyc files, please enter 'pyc' only: ").split(',')
                    print(ignoreExt)
                    ignoreNames = input("Enter the file names you want to ignore (separated by a comma (,)): ")
                    files = []
                    for r, d, f in os.walk(repo_dir):
                        for i in f:
                            if i.split('.')[-1] in ignoreExt:
                                continue
                            if i in ignoreNames.split(','):
                                continue
                            files.append(i)
                else:
                    files = command[1:]
                commands.add(repo_dir, files)
            except IndexError:
                print("Please specify the files to be added. Use 'add *' in case you want to add all files")

        if cmd == "commit":
            commands.commit(repo_dir, repo_name)

        if cmd == "logs":
            os.chdir(repo_dir+'/.vcr')
            logs = open("logs.txt")
            for i in logs.read().split('\n'):
                print(i)

        if cmd == "rollback":
            id = input("Enter the commit ID: ")
            commands.rollback(repo_dir, repo_name, id)
        if cmd == "help":
            print("""\nChoose an operation from the ones below\n
    init
    add
    commit
    rollback
    logs
    quit\n""")
        
        if cmd == "quit":
            e = True


def on_commit():
    commit_window = tk.Toplevel(root)
    commit_window.title("Commit Changes")
    commit_window.minsize(300, 150)  # Set a minimum window size for the commit window

    # Function to close the commit window
    def close_commit_window():
        messg = commit_text_entry.get()
        commands.commit(repo_dir, repo_name, messg)
        title_label.config(text = "Commit Successful")
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
        filename = add_text_entry.get().split(" ")
        files = []
        try:
            if filename[0] == "*":
                # ignoreExt = input("Enter the file extensions you want to ignore (separated by a comma (,). \n For example, if you wish to ignore all .pyc files, please enter 'pyc' only: ").split(',')
                # print(ignoreExt)
                # ignoreNames = input("Enter the file names you want to ignore (separated by a comma (,)): ")
                files = []
                for r, d, f in os.walk(repo_dir):
                    for i in f:
                        # if i.split('.')[-1] in ignoreExt:
                        #     continue
                        # if i in ignoreNames.split(','):
                        #     continue
                        files.append(i)
            else:
                files = filename[0:]
            commands.add(repo_dir, files)
        except IndexError:
            print("Please specify the files to be added. Use 'add *' in case you want to add all files")

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
    os.chdir(repo_dir+'/.vcr')
    logs = open("logs.txt")
    for i in logs.read().split('\n'):
        print(i)

    #log_label = tk.Label(log_window, text="")
    

def on_rollback():
    rb_window = tk.Toplevel(root)
    rb_window.title("Rollback")
    rb_window.minsize(300, 150)  # Set a minimum window size for the commit window

    # Function to close the commit window
    def close_rb_window():
        id = rb_text_entry.get()
        commands.rollback(repo_dir, repo_name, id)
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
        x = init_text_entry.get()
        global repo_dir, repo_name
        repo_dir = x.replace("\\", "/")
        repo_name = repo_dir.split("/")[-1].replace(" ", "_")
        
        print(repo_dir, repo_name)
        cmd = "init"
        if cmd == "init":
            print("INIT YAY")
            try:
                commands.init(repo_name, repo_dir)
                os.chdir(os.path.join(repo_dir, ".vcr"))
            except FileExistsError:
                print("This folder is already a repository")
        try:
            os.chdir(os.path.join(repo_dir, ".vcr"))
        
        except:
            pass
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

    init_button = tk.Button(button_frame, text="Initialize", command=get_info, width=10, height=1)
    init_button.pack(side=tk.LEFT, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", command=close_init_window, width=10, height=1)
    cancel_button.pack(side=tk.LEFT, padx=5)

def on_use_current_path():
    print("""\nChoose an operation from the ones below\n
    init: Initialize the repository. Needed for 1st time setup
    add: list of files to be tracked for changes
    commit: Save changes of all files being tracked
    rollback: Rollback to the previous version (specified by commit ID)
    logs: Display detailed logs of transactions commited\n""")

# Create the main application window
root = tk.Tk()
root.title("Version Control System")
root.minsize(500, 300)  # Set a minimum window size

repo_dir=''
repo_name=''
help_text  ="""\nChoose an operation from the ones below\n
    init
    add
    commit
    rollback
    logs
    quit\n"""

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
use_current_path_button = tk.Button(root, text="Help", command=on_use_current_path, width=20, height=2)
use_current_path_button.pack(pady=10)

root.mainloop()
