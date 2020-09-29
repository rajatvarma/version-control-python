import shutil
import os
from os import path
track = ()
ver = 1


if path.exists("temps"):
    pass
else:
    os.mkdir("temps")


temp_path = os.path.join(os.path.realpath("temps"))
def_path = os.getcwd()

        


def init():
    import os
    from os import path
    folder = input("Name of folder where database will be stored--> ")
    try:
        os.mkdir(folder)
        if path.exists(folder):
            print("Folder Created")
    except:
        print("Folder not created")


def add():
    global track
    global track_val
    folder_1 = input("Enter parent folder --> ")
    folder = input("Enter folder/file name --> ")
    ext = input("Enter file extention(Blank for Folder) --> ")
    path_to_watch = os.path.realpath(folder_1)
    if folder != "*":
        path_to_watch = os.path.join(path_to_watch, folder+ext)
        if path.exists(path_to_watch):
            pass
        else:
            print("file does not exist")
            add()
   
    os.chdir(def_path)
    os.chdir("temps")

    if path.exists(folder_1+"_temp"):
        os.chdir(folder_1+"_temp")
        if path.exists(folder+"_temp"):
            print("exists")
            pass
        else:
            os.mkdir(folder+"_temp")
            os.chdir(folder+"_temp")
    else:
        os.mkdir(os.path.realpath(folder_1)+"_temp")
        os.chdir(folder_1+"_temp")
        os.mkdir(folder+"_temp")
        os.chdir(folder+"_temp")
    os.chdir(def_path)
    os.chdir("temps")
    track_val = []
    track_val.append(folder)
    track_val.append(path_to_watch)
    track = list(track)
    track.append(track_val)
    track = tuple(track)

                
            
    os.chdir(def_path)

def show():
    try:
        
        for i in track:
            print(i[0])
    except:
        print(track)


def commit():
    import random
    folder_1 = input("Enter parent folder --> ")
    folder = input("Enter folder/file--> ")
    ext = input("Enter file extention(Enter folder to replace a folder) --> ")
    os.chdir("temps")
    if path.exists(folder_1+"_temp"):
        os.chdir(folder_1+"_temp")
        if path.exists(folder+"_temp"):
                os.chdir(folder+"_temp")
                x = os.getcwd()
                y = os.path.join(def_path, folder_1)
                z = os.path.join(x, folder)
                os.chdir(y)
                hcode = hex(random.randint(100000,999999))
                hcode = hcode[2::]
                if ext != "folder":
                    shutil.copy(folder+ext, x)
                    os.chdir(x)
                    os.rename(folder+ext,hcode+ext)
                    print("file")
                else:
                    shutil.copytree(folder, z)
                    os.chdir(x)
                    print(x)
                    os.rename(folder,hcode)
                    print("folder",folder)
    else:
        
        print("error")
    os.chdir(def_path)




def rollback(commit_id):
    file = input("Enter file/folder name --> ")
    ext = input("Enter file type(Blank to replace a folder) --> ")
    folder = input("Enter parent folder --> ")
    os.chdir(def_path)
    os.chdir(folder)
    print(os.getcwd())
    if path.exists(file+ext):
        os.remove(file+ext)
    else:
        print("Not there")
        pass
    os.chdir(def_path)
    os.chdir("temps/"+folder+"_temp/"+file+"_temp/")
    path = os.path.abspath(file+"("+commit_id+")")
    shutil.copy(file+ext+"("+commit_id+")",path1)





def reset():
    global track
    global track_val
    folder_1 = input("Enter parent folder --> ")
    folder = input("Enter folder/file name --> ")
    ext = input("Enter file extention(Blank for Folder) --> ")
    for i in range(len(track)):
        if track[i][0] == folder:
            os.chdir("temps")
            os.chdir(folder_1+"_temp")
            if ext == '':
                shutil.rmtree(folder+ext+"_temp")
            else:
                os.remove(folder+ext+"_temp")
        else:
            print("Folder is not being tracked")
    os.chdir(def_path)

    
    
    
