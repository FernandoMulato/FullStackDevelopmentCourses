import bd.data_base as sqldb

obj_database = sqldb.cls_Database(**sqldb.dct_database_access)

obj_database.op_show_db()

obj_database.op_close()
