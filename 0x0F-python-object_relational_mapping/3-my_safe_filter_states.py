#!/usr/bin/python3
import MySQLdb
from sys import argv

""" This module lists entries in a table that match a name sans SQLi"""

if __name__ == '__main__':
    #argv 1 :username agrv 2: password argv 3: database name
    sql = MySQLdb.connect(host="localhost",port=3306,user=argv[1], passwd=argv[2], db=argv[3])

    # Create a cursor object to interact with the database
    cur = sql.cursor()
    # Extract the name from the command line argument and prevent SQL injection
    x = argv[4].split("'")[0]

    # Build the SQL query to select entries from the 'states' table
    s = "SELECT * FROM states WHERE name=%s  ORDER BY id ASC"
    cur.execute(s, (x,))
    row = cur.fetchone()
    # Iterate through the rows and print those that match the specified name
    if row:
        if row[1] ==argv[4]:
            print(row)
    cur.close()
    sql.close()
