def main():
    print("Hello! My love")


    get_user_expense()

    Check_the_expense()

    sumerise_expense()
    

def get_user_expense():
    print("Collect the user expense.")
    expensename=input("Enter your Expense Category:")
    expenseAmount=float(input("Enter the amount:"))
    print(f"You have enter{expensename},{expenseAmount}")

    expenseCategory=[]
def Check_the_expense():
    print("Check the expense!")
def sumerise_expense():
    print("Summerize the price.!")

    while True:
        user_choice=int(input("Enter your choich from 1-4:"))

        if user_choice ==1:
            get_user_expense()
        elif user_choice ==2:
            Check_the_expense()
        elif user_choice==3:
            sumerise_expense()
        elif user_choice ==4:
            break
        




if __name__=="__main__":
    main()
