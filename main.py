import budget

food = budget.Category("Food")
food.deposit(5000, "initial deposit")
food.withdraw(100, "groceries")
food.withdraw(200, "Supper")
print(food.compute_balance())
clothing = budget.Category("Clothing")
food.transfer(500, clothing)
clothing.withdraw(100)
clothing.withdraw(200)
auto = budget.Category("Auto")
auto.deposit(10000, "initial deposit")
auto.withdraw(150)

print(food)
print(clothing)