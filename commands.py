import shutil
import os
from os import path
import sql_wrapper


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


def commit():
    open(fname, "r")
    for line_number in range(len(f.split('\n'))):
        if line not in staged_file:
            additions.append(line)
        else:
            deletions.append(line)



def rollback(commit_id):
    return none


def reset():
    return none
