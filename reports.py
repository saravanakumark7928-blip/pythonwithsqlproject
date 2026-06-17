from database import cursor
import csv


def total_sales():

    cursor.execute("SELECT SUM(Price) FROM Orders")

    result = cursor.fetchone()

    print("Total Sales:",result[0])


def export_csv():

    cursor.execute("SELECT * FROM Orders")

    data = cursor.fetchall()

    with open("orders.csv","w",newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["OrderID","CustomerName","Item","Price"])

        writer.writerows(data)

    print("Data exported to orders.csv")