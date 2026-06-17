import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sax.in07",
    database="HotelDB"
)

cursor = db.cursor()

print("Database Connected Successfully")