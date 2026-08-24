class ExpenseManager:

    def __init__(self,items,amount, category, description, data_time):
        self.expenses=items
        self.amounts=amount
        self.category=category
        self.des=description
        self.details=data_time

    def cal_expanse(self, amount):
        
        self.amounts+=amount

    def show_expense(self):
        print("Item:", self.expenses)
        print("Amount:", self.amounts)
        print("Category:", self.category)
        print("Description:", self.des)
        print("Date & Time:",self.details)


objexpense=ExpenseManager(1,250, "FOOD", "Dinner","17th Aug- 10:12PM")
print(objexpense.show_expense())
objexpense.cal_expanse(23)
print(objexpense.show_expense())
