.

import os
from os import path
track = ()
track_val = []
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
    import shutil
    folder = input("Name of folder where database will be stored--> ")
    try:
        os.mkdir(folder)
        if path.exists(folder):
            print("Folder Created")
    except:
        print("Folder not created")


def add():
    import os
    from os import path
    import shutil
    import time
    global track
    global track_val
    folder_1 = input("Enter parent folder --> ")
    folder = input("Enter folder/file name --> ")
    path_to_watch = os.path.realpath(folder_1)
    if folder != "*":
        path_to_watch = os.path.join(path_to_watch, folder)
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
    tstamp = time.time()
    track_val.append(folder)
    track_val.append(path_to_watch)
    track_val.append(tstamp)
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
    import shutil
    import os
    import time
    folder_1 = input("Enter parent folder --> ")
    ext = input("Enter file extention(Enter folder to replace a folder) --> ")
    folder = input("Enter folder/file--> ")
    os.chdir("temps")
    if path.exists(folder_1+"_temp"):
        os.chdir(folder_1+"_temp")
        if path.exists(folder+"_temp"):
                os.chdir(folder+"_temp")
                x = os.getcwd()
                y = os.path.join(def_path, folder_1)
                z = os.path.join(x, folder_1)
                os.chdir(y)
                tstamp = str(time.time())
                if ext != "folder":
                    shutil.copy(folder, x)
                    os.chdir(x)
                    os.rename(folder,folder+"("+tstamp+")"+ext)
                    print("file")
                else:
                    shutil.copytree(folder, z)
                    os.rename(folder,folder+"("+tstamp+")"+ext)
                    print("folder")
                    print(z)
    else:
        
        print("error")
    os.chdir(def_path)




def rollback(commit_id):
    file = input("Enter file/folder name --> ")
    ext = input("Enter file type(Enter folder to replace a folder) --> ")
    if str.lower(ext) != "folder":
        ext = ".txt"
    folder = input("Enter parent folder --> ")
    import shutil
    import os
    from os import path
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

