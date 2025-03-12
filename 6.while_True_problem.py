'''#1. write a program to create a billing system at super market
while True :
    name = input("Enter Customer's Name = ")
    total = 0
    
    while True :
        print("Enter the amount and quantity")
        amount = float(input("Enter amount = "))
        quantity = float(input("Enter quantity = "))
        total  += amount * quantity 
        repeat = input("Do you want to add more items? (yes/no) : ")
        if repeat == "no" or repeat ==  "No" :
            break 
        
    print("_"*40)
    print("Name = ",name)
    print("Amount to be paid = ",total)
    print("_"*40)
    print("*****Happy Shopping*****")
    repeat1 = input("Do you want to go to next custmer? (yes/no) : ")
    if repeat1 == "no" or repeat1 == "No" :
      break      
        
    '''