import shutil
import os
from os import path
import sql_wrapper

#C:/Users/rajat/Desktop/textfiles

track = ()
ver = 1


def init(dir):
    os.mkdir(os.path.join(dir, ".vcr"))
    sql_wrapper.init_repo(dir.split("/")[-1])


def add(dir, file_list):
    try:
        os.chdir(os.path.join(dir, ".vcr"))
        f = open("files.txt", "a")
        temp_file = open("files.txt", "r")
        tracking_list = temp_file.read()
        temp_file.close()
        
        allfiles = []
        for r, d, i in os.walk(dir):
            allfiles.append(i)
        for i in file_list:
            f.write(i+"\n")
    
    except FileNotFoundError:
        print("This directory has not been initialised as a repository. Run init to intitlialise it.")


def show():
    try:        
        for i in track:
            print(i[0])
    except:
        print(track)


def commit(dir):
    os.chdir(os.path.join(dir, ".vcr"))
    f = open("files.txt", "r")
    msg = input("enter message (optional)")
    if msg == '':
        msg = "none"
    import random
    for fname in f.readlines():
        os.chdir(dir)
        if fname[0] != "." and fname != "files.txt":
            openfile = open(fname[:-1], "r")
            change = openfile.read()
            
            random_number = random.randint(0, 16777215)
            hex_number = str(hex(random_number))
            hex_number ='#'+ hex_number[2:]
            sql_wrapper.commit(dir.split("/")[-1], hex_number, msg, change, fname)
            os.chdir(os.path.join(dir, ".vcr"))
