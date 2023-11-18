#!/usr/bin/python3
import MySQLdb
from sys import argv
""" This module lists entries in a table that match a name without SQL injection vulnerabilities """
if __name__ == '__main__':
     # argv 1: username, argv 2: password, argv 3: database name
     sql = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
     
     # Create a cursor object to interact with the database
     cur = sql.cursor()
     
     #Extract the name from the command line argument and prevent
     state_name = argv[4].split("'")[0]
     
     #Build a query with a parametiried statement and prevent sql injectio
     s = "SELECT DISTINCT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name=%s"
     
     cur.execute(s,(state_name,))
     #Fetch  the  first row returned by the query
     rows = cur.fetchall()

     #Iterate through the rows and print those that match the specified name
     if rows:
         cities = ', '.join(row[0] for row in rows)
         print(cities)
cur.close()
sql.close()
