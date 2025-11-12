# Imports
import pymysql

# Create the connection object to the server
dct_database_access = {"host" : "localhost",
    "user" : "root",
    "password" : "********"
    }

class cls_Database:
    # Constructor
    def __init__(self, **kwargs):
        self.att_conector = pymysql.connect(**kwargs)
        self.att_cursor = self.att_conector.cursor()

    # Makes any query to the server
    def op_query(self, prm_sql):
            self.att_cursor.execute(prm_sql)
            var_result = self.att_cursor.fetchall()
            return var_result

    # Displays the server databases
    def op_show_db(self):
            self.att_cursor.execute("SHOW DATABASES;")
            for bd in  self.att_cursor:
                print(bd)

    # Closes the connection
    def op_close(self):
        self.att_conector.close()

    # Delete a database
    def op_delete_db(self, prm_db_name):
        self.att_cursor.execute(f"DROP DATABASE {prm_db_name};")
        print(f"Database {prm_db_name} was successfully deleted")

