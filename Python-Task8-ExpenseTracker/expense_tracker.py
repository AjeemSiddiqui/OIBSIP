balance = 0
history = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        income = float(input("Enter income amount: "))
        balance += income
        history.append(f"Income: +₹{income}")

    elif choice == "2":
        expense = float(input("Enter expense amount: "))
        balance -= expense
        history.append(f"Expense: -₹{expense}")

    elif choice == "3":
        print(f"\nCurrent Balance: ₹{balance}")

    elif choice == "4":
        print("\nTransaction History:")
        for item in history:
            print(item)

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")