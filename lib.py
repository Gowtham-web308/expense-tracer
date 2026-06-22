
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime 

FILE_NAME = "expense.csv"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE_NAME, index=False)

def add_transaction():
    date = datetime.datetime.now()
    category = input("Enter category :")
    amount = float(input("Enter amount :")) 
     
    new_data = pd.DataFrame({
        "Date" : [date.strftime("%x")],
        "Category" : [category],
        "Amount" : [amount]
    })

    new_data.to_csv(FILE_NAME, mode="a", header=False, index=False)
    print("Expense Added Successfully!")

def view_transaction():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expense found!")
    else:
        print(df)

def balance_calculation():
    df = pd.read_csv(FILE_NAME)
    print(f"Total expense ₹{df['Amount'].sum()}")
    print(f"Average expense ₹{df['Amount'].sum() / len(df['Amount'])}")
    print(f"High expense ₹{df["Amount"].max()}")
    print(f"Low expense ₹{df["Amount"].min()}")

def category_report():
    df = pd.read_csv(FILE_NAME)
    report = df.groupby("Category")["Amount"].sum()
    print('\n Expense by category')
    print(report)

def expense_chart():
    df = pd.read_csv(FILE_NAME)
    plt.subplot(1,2,1)
    plt.barh(df["Category"],df["Amount"])
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expense Bar Chart")
    plt.show()

    plt.subplot(1,2,2)
    plt.pie(df["Amount"],labels= df["Category"])
    plt.legend(title = "Expense Pie Chart")
    plt.show()

while True:

    print("="*45 + "EXPENSE TRACKER" + "="*54)
    print("1. Add Transcation | 2. View Transcation | 3. Balance Calculation | 4. Category Report | 5. Expense Chart | 6. Exit")
    print("-"*114)
    choice = input("Enter the choice : ")

    match choice:
       case "1":
           add_transaction()
       case "2":
           view_transaction()
       case "3":
            balance_calculation()
       case "4":
            category_report()
       case "5":
            expense_chart()
       case "6":
            print("Good Bye !")
