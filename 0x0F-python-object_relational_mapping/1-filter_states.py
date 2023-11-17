#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
        # argv: 1 is username, 2 is pass, 3 is db name
            sql = MySQLdb.connect(host="localhost", port=3306,
                                              user=argv[1], password=argv[2],db=argv[3])
            curs =sql.cursor()
            query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
            curs.execute(query)

            rows = curs.fetchall()
            for row in rows:
                if row[1] [0] =="N":
                    print(row)
            curs.close()
            sql.close
