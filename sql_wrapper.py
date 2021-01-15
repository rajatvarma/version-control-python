import mysql.connector
password = input("Enter your MySQL password: ")
conn = mysql.connector.connect(host="localhost", user="root", password=password)
cur = conn.cursor()

try:
    cur.execute("CREATE DATABASE versioncontrolrepositorydb")
    conn.commit()
except:
    cur.execute("USE versioncontrolrepositorydb")
    conn.commit()

try:
    cur.execute("CREATE TABLE repositories_all (name varchar(100), location varchar(100))")
    conn.commit()
except:pass

def init_repo(repo_name, path):
    query = '''CREATE TABLE %s (commit_id varchar(10), file_name varchar(100), message varchar(200), contents varchar(65000)) ''' % repo_name
    query2 = '''INSERT INTO repositories_all ('%s', '%s')''' % (repo_name, path)
    print(query)
    cur.execute(query)
    cur.execute(query2)
    conn.commit()


def commit(repo_name, commit_id, message, changes, filename):
    query = '''INSERT INTO %s VALUES ('%s', '%s', '%s', "%s")''' % (repo_name, commit_id, filename, message, changes)
    cur.execute(query)
    conn.commit()

def show():
    query = "SELECT * FROM repositories_all"
    cur.execute(query)
    return cur.fetchall()

def rollback(rname, id):
    query = "SELECT file_name, contents FROM %s WHERE commit_id = '%s'" % (rname, id)
    print(query)
    cur.execute(query)
    return cur.fetchall()