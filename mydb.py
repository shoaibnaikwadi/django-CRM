import mysql.connector

dataBase = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    password = 'Shoaib@123',
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE dbone")

print("all done!")