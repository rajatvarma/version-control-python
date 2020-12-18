import shutil
import os
from os import path
import sql_wrapper


track = ()
ver = 1


def init(dir):
    os.mkdir(os.path.join(dir, ".vcr"))
    
    #sql_wrapper.init_repo(dir.split("/")[-1])


def add(dir, file_list):
    try:
        os.chdir(os.path.join(dir, ".vcr"))
        f = open("files.txt", "a")
        temp_file = open("files.txt", "r")
        tracking_list = temp_file.read()
        temp_file.close()
        
        for i in file_list:
            if i not in tracking_list:
                f.write(i+"\n")
                
                '''
                if i in os.walk(dir):
                    f.write(i+"\n")
                else:
                    print("This file does not exist in this directory")
                '''
    
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
    print(os.getcwd())
    f = open("files.txt", "r")
    for fname in f.readlines():
        print(fname)
        os.chdir('..')
        print(os.getcwd())
        open(fname, "r")
        change = fname.readlines()
        msg = input("enter message (optional)")
        if msg == '':
            msg = "none"
        import random
        random_number = random.randint(0,16777215)
        hex_number = str(hex(random_number))
        hex_number ='#'+ hex_number[2:]
        sql_wrappeer.commit(dir,hex_number ,msg , change, fname)
        os.chdir(os.path.join(dir, ".vcr"))
