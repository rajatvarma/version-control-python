import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password=input("Enter your MySQL password"))
cur = conn.cursor()

try:
    cur.execute("CREATE DATABASE versioncontrolrepositorydb")
except:
    cur.execute("USE versioncontrolrepositorydb")


def init_repo(repo_name):
    cur.execute('''CREATE TABLE %s (commit_id varchar(10), file_name varchar(100), message varchar(200), lno int, addition varchar(250), deletion varchar(250))''' % repo_name)


def commit(repo_name, commit_id, message, changes):
    for line in changes:
        cur.execute('''INSERT INTO %s VALUES ('%s', '%s', '%s', %d, '%s', '%s' )''')
        