import budget
from budget import create_spend_chart

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

entertainment = budget.Category("Entertainment")

# food = budget.Category("Food")
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)

categories = [food,auto,clothing]

print(list(category.totalWithdraw for category in categories))
print(list(category.totalDeposit for category in categories))

totalFunds = sum(category.totalDeposit for category in categories)
percentages = list((category.totalWithdraw/totalFunds ) for category in categories)

      
print(totalFunds, percentages)