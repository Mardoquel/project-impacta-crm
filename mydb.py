import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mardoquel1'
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE crm")