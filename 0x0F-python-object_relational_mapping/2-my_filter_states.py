#!/usr/bin/python3
import MySQLdb
import sys

def main():
#Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        db = MySQLdb.connect(
                 host="localhost",
                 port=3306,
                 user=username,
                 passwd=pasword,
                 db=database
                 )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name='{}' ORDER BY id".format(state_name)

        try:
            cursor.execute(query)
            row = cursor.fetchone()
            if row:
                print(row)
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            cursor.close()
            db.close()
        if __name__ == "__main__":
                main()
