'''
1. Create code that stores budget info into text file
2. Create main Import budget, retrieve from food txt and store
'''

from budget import Budget

with open("food.txt", "r") as file1:
    amount = int(file1.read())
food = Budget(amount)

with open("bills.txt", "r") as file1:
    amount = int(file1.read())
bills = Budget(amount)

control = True

while control:
    
    input1 = int(input("Menu: \nEnter 1 for Food Options \nEnter 2 for Bills Options \nEnter 0 to Exit \nEnter Option: "))
    
    control_bills = True
    
    if input1 == 1:
        
        control_food = True
        
        while control_food == True:
            
            food_input= int((input("Food Account: \nEnter 1 To Deposit \nEnter 2 to Withdraw \nEnter 3 to Transfer to Bills \nEnter 4 For Balance \nEnter 0 to Exit \nEnter Option: ")))
            
            if food_input == 1:
                #deposit into food account
                food = Budget(500)
                
            elif food_input == 2:
                #withdraw from food account
                food.withdraw

            elif food_input == 3:
                #transfer from food to bills
                bills.deposit(food.withdraw(50))

            elif food_input == 4:
                #print food Balance
                print(food)

            elif food_input == 0:
                control_food = False

            else:
                print("Invalid Option")
    elif input1 == 2:
        
        control_bills = True
        
        while control_bills == True:

            bills_input= int((input("Bills Account: \nEnter 1 To Deposit \nEnter 2 to Withdraw \nEnter 3 to Transfer to Food \nEnter 4 For Balance \n Enter 0 to Exit \n Enter Option: ")))
            
            if bills_input == 1:
                #deposit into bills account
                bills = Budget(200)
            
            elif bills_input == 2:
                #withdraw from bills account
                bills.withdraw(50)
            
            elif bills_input == 3:
                #transfer from bills to food
                food.deposit(bills.withdraw(50))

            elif bills_input == 4:
                #print food Balance
                print(bills)
            
            elif bills_input == 0:
                control_bills = False
            
            else:
                print("Invalid Option")
    
    elif input1 == 0:
        control = False
    
    else:
        print("Invalid Option")
    
    # if food:
    #     

    #     file1= open("txt_budget.txt","w")
    #     contents = contents + "\n"
    #     file1.write(contents)
    #     file1.write(food)
    #     file1.close()

    # if bills:
    #     file1 = open("txt_budget.txt", "r")
    #     contents = file1.read()
    #     file1.close()

    #     file1= open("txt_budget.txt","w")
    #     contents = contents + "\n"
    #     file1.write(contents)
    #     file1.write(bills)
    #     file1.close()


