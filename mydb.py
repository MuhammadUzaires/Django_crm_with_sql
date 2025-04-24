import mysql.connector

dataBases=mysql.connector.connect(
    
    host='localhost',
    user='root',
    passwd='root'
)

cursorObject=dataBases.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")