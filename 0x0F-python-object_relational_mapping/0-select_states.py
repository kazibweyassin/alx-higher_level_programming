#!/usr/bin/python3
import MySQLdb
import sys

""" This scripts lists all states from the database"""

def get_states(username, password, database):
    """This function prints the states"""
    database = MySQLdb.connect(user=username, passwd=password, db=database)
    cur = database.cursor()
    cur.execute("SELECT * FROM states")
    items = cur.fetchall()
    for item in items:
        print(item)
    cur.close()
    database.close()


if __name__ == '__main__':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    get_states(usr, pwd, db)
