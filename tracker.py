import csv
from datetime import datetime

with open("expenses.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Category", "Amount", "Description",])
f.close

def add_expense(date, category, amount, description):
    with open("expenses.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])
    f.close

def get_expense(date, category, amount, description):
    with open("expenses.csv", "r") as f:
        rows = csv.reader(f)
        for i in rows:
            print(i)
    f.close

print("--- Expense Tracker ---")
print(" 1. Add Expenses\n 2. Get Expenses\n 3. Exit")
flag = 1
while (flag == 1):
    a = int(input(" Enter Menu Choice : "))
    if a == 1:
        #date
        date_str = input(" Enter Date (DD-MM-YYYY) : ")
        if date_str == "":
            date_str = datetime.today().strftime("%d-%m-%Y")
        try:
            date_obj = datetime.strptime(date_str, "%d-%m-%Y")
            date_str = date_obj.strftime("%d-%m-%Y")
        except ValueError:
            print(" Date Error. Try Again.")
        #category
        category = input(" Enter Category : ")
        if category == "":
            category = "Other"
        #amount
        amount = int(input(" Enter Amount : ") or 0)
        #description
        description = input(" Enter Description : ")
        add_expense(date_str,category,amount,description)
        continue
    elif a == 2:
        get_expense
    elif a == 3:
        flag = 0
    else:
        print(" Invalid Option. Try Again.")