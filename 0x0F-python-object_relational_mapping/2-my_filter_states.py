#!/usr/bin/python3
'''
    takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
'''
import sys
import MySQLdb


if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = connection.cursor()
    state_name = sys.argv[4]
    cur.execute("SELECT * FROM states
                WHERE name='" + state_name + "' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connection.close()
