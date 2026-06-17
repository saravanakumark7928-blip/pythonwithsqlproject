from database import db, cursor

def add_order():

    order_id = int(input("Enter Order ID: "))
    name = input("Enter Customer Name: ")
    item = input("Enter Food Item: ")
    price = int(input("Enter Price: "))

    query = "INSERT INTO Orders VALUES (%s,%s,%s,%s)"
    values = (order_id,name,item,price)

    cursor.execute(query,values)
    db.commit()

    print("Order Added Successfully")


def view_orders():

    cursor.execute("SELECT * FROM Orders")

    result = cursor.fetchall()

    print("\nAll Orders")
    for row in result:
        print(row)


def update_order():

    order_id = int(input("Enter Order ID to update: "))
    item = input("Enter new food item: ")
    price = int(input("Enter new price: "))

    query = "UPDATE Orders SET Item=%s, Price=%s WHERE OrderID=%s"
    values = (item,price,order_id)

    cursor.execute(query,values)
    db.commit()

    print("Order Updated Successfully")


def delete_order():

    order_id = int(input("Enter Order ID to delete: "))

    query = "DELETE FROM Orders WHERE OrderID=%s"

    cursor.execute(query,(order_id,))
    db.commit()

    print("Order Deleted Successfully")


def search_order():

    name = input("Enter Customer Name: ")

    query = "SELECT * FROM Orders WHERE CustomerName=%s"

    cursor.execute(query,(name,))
    result = cursor.fetchall()

    for row in result:
        print(row)


def calculate_bill():

    name = input("Enter Customer Name: ")

    query = "SELECT SUM(Price) FROM Orders WHERE CustomerName=%s"

    cursor.execute(query,(name,))
    result = cursor.fetchone()

    print("Total Bill:",result[0])