#!/usr/bin/python3
'''
 takes in the name of a state as an argument
 and lists all cities of that state
'''
import sys
import MySQLdb


if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = connection.cursor()
    state_name = sys.argv[4]
    cur.execute("""
            SELECT cities.name
            FROM cities INNER JOIN states ON states.id = cities.state_id
            WHERE states.name = %s
            """, (state_name,))
    rows = cur.fetchall()
    i = 0
    for i, element in enumerate(rows):
        if (i == len(rows) - 1):
            print("%s" % element)
        else:
            print("%s, " % element, end="")
    cur.close()
    connection.close()
