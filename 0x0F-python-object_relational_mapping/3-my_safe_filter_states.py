#!/usr/bin/python3
"""
  This is a script that lists all states from the database hbtn_0e_0_usa
    using MySQLdb ORM
"""


def select_states(username, password, database, name):
    """ Function that print the states """
    import MySQLdb

    database = MySQLdb.connect(user=username, passwd=password, db=database)
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (name,))
    items = cur.fetchall()
    for item in items:
        if item[1] == name:
            print(item)
    cur.close()
    database.close()


if __name__ == "__main__":
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]
    select_states(usr, pwd, db, name)
