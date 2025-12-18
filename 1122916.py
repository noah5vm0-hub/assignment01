import matplotlib.pyplot as plt

records = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    records.append({
        "date": date,
        "category": category,
        "amount": amount
    })
    print("Expense added.\n")

def show_pie_chart():
    if not records:
        print("No data to display.\n")
        return

    summary = {}
    for r in records:
        summary[r["category"]] = summary.get(r["category"], 0) + r["amount"]

    plt.figure()
    plt.pie(summary.values(), labels=summary.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution by Category")
    plt.show()   # 關掉視窗後，程式會回到選單

while True:
    print("=== Expense Tracker ===")
    print("1. Add expense")
    print("2. Show pie chart")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_pie_chart()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")
