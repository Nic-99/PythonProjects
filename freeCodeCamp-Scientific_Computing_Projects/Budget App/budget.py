from tabnanny import check

class Category:
    
    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.ledger = []
        self.funds = 0
        self.totalDeposit = 0
        self.totalWithdraw = 0
    
    def __str__(self):
        res = f'{self.categoryName:*^30}' + "\n"
        for val in self.ledger:
            amount = "{:0.2f}".format(val["amount"])
            line = (val["description"][:29-len(amount)]+' ') if len(val["description"]) > (30-len(amount)) else val["description"]
            res += f'{line:<{27-len(str(val["amount"]))}}{amount}' + "\n"
        res += "Total: "+str(self.funds)
        return res
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount
        self.totalDeposit += amount

    def withdraw(self, amount, description=""):
        if  self.check_funds(amount):
            self.funds = self.funds - amount 
            self.totalWithdraw += amount
            self.ledger.append({"amount": (amount*(-1)), "description": description})
            return True
        else: return False

    def get_balance(self):
        return self.funds
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount,"Transfer to "+category.categoryName)
            category.deposit(amount, "Transfer from "+self.categoryName)
            return True
        else: return False

    def check_funds(self, amount):
        if self.funds >= amount: return True
        else: return False


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    graph = "100| \n 90| \n 80| \n 70| \n 60| \n 50| \n 40| \n 30| \n 20| \n 10| \n  0| \n"
    matrix = [
        ["100|"],
        [" 90|"],
        [" 80|"],
        [" 70|"],
        [" 60|"],
        [" 50|"],
        [" 40|"],
        [" 30|"],
        [" 20|"],
        [" 10|"],
        ["  0|"],
        ["-"],
        [""]
    ]
    totalFunds = sum(category.totalDeposit for category in categories)
    percentages = list((category.totalWithdraw / totalFunds *100) for category in categories)
    return ""