# How to create MySQL database backups

# Exporting databases with MySQL workbench
# 1. Menu option -> Server -> Data Export
# 2. Select the database with all or some tables (functions, procedures, events or triggers can also be selected)
# 3. Export to Dump Project Folder: (example) D:\copies-SQL\world
# 4. Star Export

# Import databases with MySQL Workbench
# 1. Menu option -> Server -> Data Import
# 2. Import to Dump Project Folder
# 3. Star Import

# Exporting databases from the console
# 1. Write in the start menu CMD
# 2. C: -> >cd C:\Program Files\MySQL\MySQL Workbench 8.0 CE\ 
# 3. C:\Program Files\MySQL\MySQL Workbench 8.0 CE>mkdir D:\copies-SQL\console
# 4. C:\Program Files\MySQL\MySQL Workbench 8.0 CE>mysqldump --user=root --password=******** --databases world > D:\copies-SQL\console\world.sql

# Delete MySQL databases from the console
# 1. C:\Program Files\MySQL\MySQL Workbench 8.0 CE>mysql -h localhost -u root -p 
# 2. mysql> DROP DATABASE world
# 3. mysql> SHOW DATABASES;

# Create MySQL databases from the console
# 1. mysql> CREATE DATABASE world 
# 2. mysql> SHOW DATABASES;
# 3. mysql> exit

# Import MySQL databases from the console
# 1. C:\Program Files\MySQL\MySQL Workbench 8.0 CE>mysql --user=root --password=******** < D:\copies-SQL\console\world.sql

# Query basic SQL from the console
# 1. C:\Program Files\MySQL\MySQL Workbench 8.0 CE>mysql -h localhost -u root -p 
# 2. mysql> USE world;
# 3. mysql> SHOW TABLES;
# 4. mysql> SHOW COLUMNS FROM city;
# 5. mysql> SELECT * FROM city WHERE population > 1000000 ORDER BY population DESC;

# Export MySQL databases from Python
import subprocess
import getpass

with open('D:\world.sql', 'w') as out:
    subprocess.Popen(f'"C:/Program Files/MySQL/MySQL Workbench 8.0 CE/"mysqldump --user=root --password={getpass.getpass()} --databases world', shell=True, stdout=out)
# 2. C: -> >cd C:\Program Files\MySQL\MySQL Workbench 8.0 CE\
# 3. Execute (terminal open)
# 4. Look at the file size if it is 0 nothing has been copied

# Import MySQL databases from Python
subprocess.Popen(f'"C:/Program Files/MySQL/MySQL Workbench 8.0 CE/"mysqldump --user=root --password={getpass.getpass()} < D:/world.sql/', shell=True)