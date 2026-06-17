from orders import add_order, view_orders, update_order, delete_order, search_order, calculate_bill
from reports import total_sales, export_csv


while True:

    print("\n------ HOTEL MANAGEMENT SYSTEM ------")
    print("1 Add Order")
    print("2 View Orders")
    print("3 Update Order")
    print("4 Delete Order")
    print("5 Search Order")
    print("6 Calculate Bill")
    print("7 Total Sales")
    print("8 Export to CSV")
    print("9 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_order()

    elif choice == 2:
        view_orders()

    elif choice == 3:
        update_order()

    elif choice == 4:
        delete_order()

    elif choice == 5:
        search_order()

    elif choice == 6:
        calculate_bill()

    elif choice == 7:
        total_sales()

    elif choice == 8:
        export_csv()

    elif choice == 9:
        print("Thank you")
        break

    else:
        print("Invalid Choice")