#!/usr/bin/python3
import MySQLdb
from sys import argv

""" This module lists entries in a table starting with N """

if __name__ == '__main__':
    # argv: 1 is username, 2 is pass, 3 is db name
    sql = MySQLdb.connect(host="localhost", port=3306,
                          username=argv[1], password=argv[2] database=argv[3])

    curs = sql.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = curs.fetchall()
    for row in rows:
        if row[1][0] == "N":
            print(row)
    curs.close()
    sql.close()
