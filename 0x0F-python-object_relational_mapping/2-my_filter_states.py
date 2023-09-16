#!/usr/bin/python3
import MySQLdb
from sys import argv

""" This module lists entries in a table that match a name"""

if __name__ == '__main__':
    # argv: 1 is username, 2 is pass, 3 is db name
    sql = MySQLdb.connect(host="localhost", port=3306,
                          username=argv[1], password=argv[2], database=argv[3])

    curs = sql.cursor()
    s = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(argv[4])
    s = s + " ASC"
    curs.execute(s)
    rows = curs.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    curs.close()
    sql.close()
