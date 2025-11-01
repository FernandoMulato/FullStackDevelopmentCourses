# Import pymysql or MySQLdb in Python
import pymysql

# Create the connection object to the server
var_connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "*************"
)

# The cursor object instance is completed
# Return and print all server databases
try:
    with var_connection.cursor() as obj_cursor:
        # Loop to read and print the databases on the server
        obj_cursor.execute("SHOW DATABASES")
        for bd in obj_cursor:
            print(bd[0])
finally:
    var_connection.close()


# With MySQLdb
import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="*************"
)
cursor = conn.cursor()

cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd[0])

cursor.close()   # ✅ Cierra el cursor
conn.close()     # ✅ Cierra la conexión
