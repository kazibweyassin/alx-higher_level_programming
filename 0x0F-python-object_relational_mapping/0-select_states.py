#!/usr/bin/python3
import MySQLdb
from sys import argv
#This module lists all entries in the table

if __name__ == '__main__':
    #argv: 1 is username, 2 is pass , 3 is db name
    sql = MySQLdb.connect(host="localhost", port=3306,
            user=argv[1], password=argv[2], db=argv[3])

    curs = sql.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    sql.close()
