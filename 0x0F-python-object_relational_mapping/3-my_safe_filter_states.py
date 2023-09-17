#!/usr/bin/python3
import MySQLdb
from sys import argv

""" This module lists entries in a table that match a name sans SQLi"""

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
        exit(1)

    # Connect to the MySQL server running on localhost at port 3306
    mydb = MySQLdb.connect(host="localhost", port=3306,
                          user=argv[1], passwd=argv[2], db=argv[3])

    cur = mydb.cursor()
    state_name = argv[4]

    # Construct the SQL query with a parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC LIMIT 1"

    try:
        # Execute the query with the state_name as a parameter
        cur.execute(query, (state_name,))
        row = cur.fetchone()
        
        if row:
            print(row)
    
    except Exception as e:
        print("Error: {}".format(e))

    finally:
        cur.close()
        mydb.close()
