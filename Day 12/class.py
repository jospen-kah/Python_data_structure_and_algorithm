class Bank:
    def __init__(self, user, amt_deposited, amt_withdrawed, date):
        self.user = user
        self.amt_deposited = amt_deposited
        self.amt_withdrawed =  amt_withdrawed
        self.date = date
        
    # Defining the withdraw method
    def withdraw(self):
        return f"Username: {self.user}\n Amount Withdraw: {self.amt_withdrawed}\n Date: {self.date}"
    # Defining the Deposited method
    def deposit(self):
        return f"Username: {self.user}\n Amount Deposited {self.amt_deposited}\n Date: {self.date}"
        
        
# p1 = Bank("jos",400,500,24)
# print(p1.withdraw())
# print(p1.deposit())

storage =  [] 
i = 0

while i < 5:
    print("Do you want to deposit or withdraw?")
    print("select:\n 1- for withdraew  \n 2-Deposited \n 3- Exit")
    choice = input("Enter your choice: ")
    if choice == "1" or choice == "2" or choice == "3":
      
        if choice == "1":
            user = input("Enter your name: ")
            amount = input("enter amount to withdraw: ")
            date = input("enter your date: ")
            users = Bank(user, 0, amount , date)
            user1=(users.withdraw())
            
        if choice == "2":
            user = input("Enter your name: ")
            amount = input("enter amount to deposit: ")
            date = input("enter your date: ")
            users = Bank(user, amount, 0 , date)
            user1= (users.deposit())
        if choice == "3":
         exit = input("Are you sure you want to exit the program 'yes' or 'no' : ")
         if exit == "yes":
            break
         else:
            continue
        print(user1)
        storage.append(user1)
        i+=1
        
        print(storage)
        
    else:
        print("\n\nEnter a choice between 1 and 2")
        continue
    
        

