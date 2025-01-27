import datetime
import time
import os
# adding date

def add_expense(category, date, money)
    try:
        date.datetime.striptime(date, '%Y-%m-%d' )
    except ValueError:
        print("Please try again with the format of YYYY-MM-DD")
        return

def main()
    cat=input("What category does this expense fall under?")
    date=input("When did this expense occur?")
    money=input("How much money did you waste on this expense?")

    try:
        add_expense(cat,date,money)
    except:
        print("One or more entries was invalid. Please try again")
        time.sleep(1)
        os.system('cls')
        main()
        
main()


    