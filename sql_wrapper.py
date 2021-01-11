import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password=input("Enter your MySQL password"))
cur = conn.cursor()

try:
    cur.execute("CREATE DATABASE versioncontrolrepositorydb")
    cur.commit()
except:
    cur.execute("USE versioncontrolrepositorydb")
    conn.commit()


def init_repo(repo_name):
    print('''CREATE TABLE %s (commit_id varchar(10), file_name varchar(100), message varchar(200), contents varchar(100000) ''' % repo_name)
    cur.execute('''CREATE TABLE %s (commit_id varchar(10), file_name varchar(100), message varchar(200), contents varchar(65000)) ''' % repo_name)
    conn.commit()


def commit(repo_name, commit_id, message, changes, filename):
    cur.execute('''INSERT INTO %s VALUES ('%s', '%s', '%s', '%s')''' % (repo_name, commit_id, filename, message, changes))
    conn.commit()

def log(repo_name):
    eoiuroirh;  