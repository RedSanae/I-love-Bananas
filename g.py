import datetime
import time
import os
# adding date

expenses=[]


def return_to_main():
    time.sleep(.5)
    os.system('clear')
    expenses.sort()
    main()

def add_expenses(date, category, money):
    cat=input("What category does this expense fall under?\n>")
    date=input("When did this expense occur?\n>")
    money=input("How much money did you waste on this expense?\n>")

    exception=None
    try:
        money=int(money)
    except:
        print("Invalid Money Input (Please only input numbers 0-9)")
        exception=True

    if not exception: 
        expenses.append(add_expense(date,cat,money))
    
    return_to_main()

def show_expenses():
    if len(expenses)>0:
        totalAmount=0
        for entry in expenses:
            print(f"Date: {entry[0]} Category: {entry[1]} Amount: ${entry[2]}")
            totalAmount+=int(entry[2])
        print(f"\nTotal: ${totalAmount}")
    else:
        print("No expenses have been recorded yet.")
    
    return_to_main()

def delete_expenses():
    print("nothing")

    return_to_main()

def main():

    options=input("[1]: Add an expense\n[2]: Show all expenses\n[3]: Delete an expense\n>")

    if options=='1':
        add_expenses()
    if options=='2':
        show_expenses()
    if options=='3':
        delete_expenses()
    else:
        print('please input a proper option')
    
main()