import mysql.connector
from mysql.connector import Error

try: 
    connection = mysql.connector.connect(
        host = 'localhost',
        port = '3307',
        user = 'root',
        passwd = 'Anni@123',
        auth_plugin='mysql_native_password',
        database = 'seproject'
    )
    mySql_Create_Table_Query = """CREATE TABLE USER ( 
                             empID VARCHAR(50) NOT NULL,
                             name varchar(250) NOT NULL,
                             password INT(11) NOT NULL,
                             PRIMARY KEY (empID)) """
    if connection.is_connected():
        print("*****Connected to database****")
        cursor = connection.cursor()
        result = cursor.execute(mySql_Create_Table_Query)

except Error as e:
    print("Error while connecting to MySQL: ", e)