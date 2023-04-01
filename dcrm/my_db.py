import mysql.connector

data_base = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
)

cursor_object = data_base.cursor()

cursor_object.execute("CREATE DATABASE elderco")

print("Database created successfully")
