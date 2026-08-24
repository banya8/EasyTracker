from datetime import datetime

class ExpenseManager:

    def __init__(self,items,amount, category, description):
        self.expenses=items
        self.amounts=amount
        self.category=category
        self.des=description
        self.details=datetime.today()

    def cal_expanse(self, amount):
        
        self.amounts+=amount

    def show_expense(self):
        print("Item:", self.expenses)
        print("Amount:", self.amounts)
        print("Category:", self.category)
        print("Description:", self.des)
        print("Date & Time:",self.details)


objexpense=ExpenseManager(1,250, "FOOD", "Dinner")
objexpense.show_expense()
print("After adding another price.")
objexpense.cal_expanse(23)
objexpense.show_expense()
print("\n")
objexpense2=ExpenseManager(2,300, "TRANSPORT", "TRAIN")
objexpense2.show_expense()

