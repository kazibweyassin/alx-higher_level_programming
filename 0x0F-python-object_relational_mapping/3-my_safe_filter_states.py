#!/usr/bin/python3
import MySQLdb
import sys
from sysmimport argv

"""Once again, write a script that takes in arguments safe from MySQL injections!"""

if __name__ == '__main__':
    connection = MySQLdb.connect(host="localhost", port=3306, username=argv[1], password=argv[2], database=argv[3])
    curs = connection.cursor()
    x =  argv[4].split("'")[0]

    s = "SELECT * FROM states WHERE name = '{}' ORDER BY id" .format(x)
    s = s + "ASC"
    curs.execute(s)
    rows = curs.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)       
    curs.close()
    connection.close()
