# Import pymysql or MySQLdb in Python
import pymysql

# Create the connection object to the server
var_connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "************",
    # Associate the SQL cursor to a specific database
    database = "american_raider"
)

# Create a MySQL database from Python
try:
    # The cursor object instance is completed
    with var_connection.cursor() as obj_cursor:
        obj_cursor.execute("CREATE DATABASE tests;")
        print("The database was successfully created.")
# Handling MySQL errors in Python
except:
    print("An error occurred while creating the database")
finally:
    var_connection.close()

# Delete MySQL databases from Python
try:
    # The cursor object instance is completed
    with var_connection.cursor() as obj_cursor:
        obj_cursor.execute("DROP DATABASE tests;")
        print("The database was deleted.")
# Handling MySQL errors in Python
except:
    print("An error occurred while deleting the database.")
finally:
    var_connection.close()

# Create MySQL tables from Python
try:
    # The cursor object instance is completed
    with var_connection.cursor() as obj_cursor:
        obj_cursor.execute("CREATE TABLE customers"
        "(id INT NOT NULL AUTO_INCREMENT,"
        "name VARCHAR(32) NOT NULL," 
        "last_names VARCHAR(64) NOT NULL,"
        "phone_number VARCHAR(9) NOT NULL,"
        "address VARCHAR(256),"
        "PRIMARY KEY (id));")
        print("The table was created correctly.")
        var_connection.commit()
# Handling MySQL errors in Python
except:
    print("There was an error creating the table.")
finally:
    var_connection.close()