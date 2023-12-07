import mysql.connector
password = "root"
conn = mysql.connector.connect(host="localhost", user="root", password=password)
cur = conn.cursor()

try:
    cur.execute("CREATE DATABASE versioncontrolrepositorydb")
    cur.execute("USE versioncontrolrepositorydb")
    conn.commit()

except:
    cur.execute("USE versioncontrolrepositorydb")
    conn.commit()

def init_repo(repo_name, path):
    try:
        query = '''CREATE TABLE %s (commit_id varchar(10), file_name varchar(100), message varchar(200), contents text) ''' % repo_name
        cur.execute(query)
        conn.commit()
    except:
        pass


def commit(repo_name, commit_id, message, changes, filename):
    query = '''INSERT INTO %s VALUES ('%s', '%s', '%s', "%s")''' % (repo_name, commit_id, filename, message, changes)
    cur.execute(query)
    conn.commit()

def rollback(rname, id):
    query = "SELECT file_name, contents FROM %s WHERE commit_id = '%s'" % (rname, id)
    cur.execute(query)
    return cur.fetchall()
