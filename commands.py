import os
from mysql.connector.connection import MySQLConnection
from mysql.connector import errors
import sql_wrapper
import random
import time


track = ()
ver = 1


def init(repo_name, dir):
    sql_wrapper.init_repo(repo_name, dir)
    '''try:
        sql_wrapper.init_repo(repo_name, dir)
    except errors.ProgrammingError:
         print("There was an internal error. However, you may continue to run your commands as normal.")'''
    temp =dir+ "/.vcr"
    os.mkdir(temp)
    os.chdir(temp)
    list_of_files = open("files.txt", "w+")
    log = open("logs.txt", "w+")


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
        files = ""
        for i in file_list:
            if i != "files.txt" and i != "logs.txt":
                print("Adding file:", i)
                f.write(i+'\n')
                files += i+", "
        print("All files added")
        f = open("logs.txt", "a")
        log = "[ADD] " + files + str(time.time()) + '\n'
        print(log)
        f.write(log)
        f.close()
    except FileNotFoundError:
        print("This directory has not been initialised as a repository. Run init to intitlialise it.")

def commit(dir, name, msg):
    os.chdir(dir+"/.vcr")
    f = open("files.txt", "r")
    #msg = input("enter message (optional)")
    if msg == '':
        msg = "none"
    allFiles = f.readlines()
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    for fname in allFiles:
        os.chdir(dir)
        if fname[0] != "." and fname[:-1] != 'files.txt' and fname[:-1] != "logs.txt":
            openfile = open(fname[:-1], "r")
            contents = openfile.read()
            changes = ""
            for char in contents:
                if char == '"':
                    changes += "&dquot"
                    continue
                elif char == "'":
                    changes += "&quot"
                    continue
                else:
                    changes += char
           
            sql_wrapper.commit(name, hex_number, msg, changes, fname[:-1])
            os.chdir(dir+'/.vcr')
            f = open("logs.txt", "a")
            log = "[COMMIT] " + str(hex_number) + " " + fname[:-1] + " " + str(time.time()) + '\n'
            f.write(log)
            f.close()

        
def rollback(dir, name, hex_code):
    os.chdir(dir)
    r = sql_wrapper.rollback(name, hex_code)
    print(r)
    file = open(r[0][0], "w")
    file.write(r[0][1])
    file.close()