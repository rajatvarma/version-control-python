import commands
import os


x = r'{}'.format(input("Enter directory path: "))
repo_dir = x.replace("\\", "/")
print(repo_dir)

repo_name = repo_dir.split("/")[-1].replace(" ", "_")
print(repo_name)

e = False
while not e:
    command = input("$>").split(" ")

    if command[0] == "init":
        try:
            commands.init(repo_name, repo_dir)
            os.chdir(os.path.join(repo_dir, ".vcr"))
        except FileExistsError:
            print("This folder is already a repository")
    try:
        os.chdir(os.path.join(repo_dir, ".vcr"))
    
    except:
        pass

    if command[0] == "add":
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

    if command[0] == "commit":
        commands.commit(repo_dir, repo_name)

    if command[0] == "logs":
        os.chdir(repo_dir+'/.vcr')
        logs = open("logs.txt")
        for i in logs.read().split('\n'):
            print(i)

    if command[0] == "rollback":
        id = input("Enter the commit ID: ")
        commands.rollback(repo_dir, repo_name, id)
    
    if command[0] == "quit":
        e = True