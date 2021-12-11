import re
def validatepin(pin):
       while True:
         global is_valid
         is_valid = False

         if (len(pin)<6 or len(pin)>12):      
           print("Not valid ! Total characters should be between 6 and 12")
           break
         elif not re.search("[A-Z]",pin):
             print("Not valid ! It should contain one letter between [A-Z]")
             break
         elif not re.search("[a-z]",pin):       
           print("Not valid ! It should contain one letter between [a-z]")
           break
         elif not re.search("[1-9]",pin):
           print("Not valid ! It should contain one letter between [1-9]")
           break
         elif not re.search("[~!@#$%^&*]",pin):    
            print("Not valid ! It should contain at least one letter in [~!@#$%^&*]")
            break
         elif re.search("[\s]",pin):    
            print("Not valid ! It should not contain any space")
            break
         
         else:

            is_valid = True
            break

class Account:
    def __init__(self,name,pin):
        self.name = name
        self.pin = pin
        self.balance = 0

    
    def depositmoney(self,amount):
        self.balance += amount
        # print ("balance is " + str(self.balance))


    def withdraw(self,withdraw):
        if self.balance < withdraw:
           print ("balance is  " + str(self.balance) + " is insufficient to complete transaction")
        else:
            self.balance -= withdraw   
            # print ("Transaction successfull and new balance is  " + str(self.balance))

username = input("Enter username:")
pin=input("Enter pin:")
validatepin(pin)
if is_valid: 
    acc1= Account(username,pin)
    print("balance is  " + str(acc1.balance))

    deposit = int(input("Enter Deposit:"))
    acc1.depositmoney(deposit)
    print ("balance is  " + str(acc1.balance))

    withdraw = int(input("Enter withdraw:"))
    acc1.withdraw(withdraw)
    print ("balance is  " + str(acc1.balance))
else:
    print("wrong pin ")
# acc1. withdraw(5000)

