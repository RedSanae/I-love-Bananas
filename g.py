import datetime
import time
import os
import multiprocessing
# adding date

expenses=[]


def return_to_main():
    time.sleep(.5)
    os.system('clear')
    expenses.sort()
    main()

def categoryInput():
    category=input("What category does this expense fall under?\n>")
    return category

def dateInput():
    date=input("When did this expense occur? (Please input with YYYY-MM-DD) \n>")

    try:
        datetime.datetime.strptime(date, '%Y-%m-%d' )
        return date
    except:
        print("Invalid Date Input format (Please input with YYYY-MM-DD)")
        time.sleep(.5)
        os.system('clear')
        dateInput()



def moneyInput():
    money=input("How much money did you waste on this expense?\n>")
    try:
        money=int(money)
        return money
    except:
        print("Invalid Money Input (Please only input numbers 0-9)")
        time.sleep(.5)
        os.system('clear')
        moneyInput()

def add_expenses():
    expenses.append([dateInput(),categoryInput(),moneyInput()])
    time.sleep(1)
    return_to_main()

def show_expenses():

    if len(expenses)>0:
        totalAmount=0
        for expense in expenses:
            print(f"Date: {expense[0]} Category: {expense[1]} Amount: ${expense[2]}")
            totalAmount+=int(expense[2])
        print(f"\nTotal: ${totalAmount}")
    else:
        print("No expenses have been recorded yet.")
    input("Type any input to proceed.\n>")
    return_to_main()

def delete_expenses():
    if len(expenses)>0:
        index=1
        print("Select an expense to delete:\n")
        for expense in expenses:
            print(f"[{index}]: Date: {expense[0]} Category: {expense[1]} Amount: ${expense[2]}")#index is used as a way to display the options to delete for the user
        try:
            index=int(input(">"))#index is reused to act as the input for which index the user wants to remove
        except:
            print("invalid input")
        index-=1#index-1 as python indexing starts with 0, so on
        if index>=0:
            del expenses[index-1]
        else:
            print("invalid input")
    else:
        print("No expenses have been listed")

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