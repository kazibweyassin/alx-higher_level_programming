#!/usr/bin/python3
import MySQLdb
import sys

def main():
    """
    Connects to a MySQL database and retrieves states matching a given name.

    Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Construct the SQL query using format
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id".format(state_name)

    try:
        # Execute the query
        cursor.execute(query)
        
        # Fetch the first row (if any) and display it in the desired format
        row = cursor.fetchone()
        if row:
            print(row)

    except Exception as e:
        print("Error: {}".format(e))

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    main()
