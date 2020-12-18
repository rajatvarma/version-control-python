import commands
import os
import mysql.connector

repo_dir = input("Enter directory name:")

e = False
while not e:
    command = input("$>").split(" ")
    if command[0] == "init":
        try:
            commands.init(repo_dir)
            os.chdir(os.path.join(repo_dir, ".vcr"))
            list_of_files = open("files.txt", "w+")
        except FileExistsError:
            print("This folder is already a repository")

    try:
        os.chdir(os.path.join(repo_dir, ".vcr"))
    except:
        pass
    if command[0] == "add":
        files = []
        if command[1] == "*":
            files = []
            for r, d, f in os.walk(repo_dir):
                files += f
        else:
            files = command[1:]
        commands.add(repo_dir, files)

    if command[0] == "commit":
        commands.commit(repo_dir)

    if command[0] == "log":
        pass

    if command[0] == "quit":
        e = True