class Budget():
    def __init__(self, balance,):
        self.balance = balance
        
    def __repr__(self):
        return f"Current Balance: {self.balance}"

    
    def withdraw(self, amount):
        self.balance -= amount
        return amount
        
    # add money to the budget
    def deposit(self, amount):
        self.balance += amount
        return amount
    
# food = Budget(500)

# bills = Budget(200)

# print(food)
# print(bills)
# bills.deposit(food.withdraw(50))
# print()
# print(food)
# print(bills)

control = True
food = 0
bills = 0

while control:
    print("Menu: click 1 for option a, or 2 for option b")
    input1 = int(input("Please enter your choice: "))
    
    if input1 == 1:
        food = Budget(500)
    elif input1 == 2:
        bills = Budget(200)
    elif input1 == 0:
        control = False
    else:
        print("Invalid Option")
    
    if food:
        print(food)
    if bills:
        print(bills)


