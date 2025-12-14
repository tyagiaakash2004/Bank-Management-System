class bank:
    #constructor
    def __init__ (self):
        pass  
    def accountopen(self):
        self.name=input("Enter your name:")
        self.fathername=input("Enter your father's name:")
        self.dateofbirth=input("Enter your date of birth:")
        self.aadharnumber=int(input("Enter your aadhar number:"))
        self.accnumber=int(input("Enter your account number:"))
        self.acc_type=input("Enter your account type:")
        self.balance=1000
        print("Account created successfully!")

    def deposit(self):
        amount=int(input("Enter amount to deposit:"))
        self.balance=self.balance+amount
        print(f"Amount {amount} deposited successfully!")
        
   
    def withdraw(self):
        amount=int(input("Enter amount to withdraw:"))
        if amount>self.balance:
                print("Insufficent balance")
        else:
            self.balance=self.balance-amount
            print(f"Amount {amount} withdrawn successfully!")
            
    
    def balanceenquiry(self):
        print(f"Your current balance is: {self.balance}")
    
data=bank()
while True:
    print("Press 1 to account opening")
    print("Press 2 to Deposit amount")
    print("Press 3 to Withdraw amount")
    print("Press 4 to Balance Enquiry")
    print("Press 5 to exit")
    a=int(input())
    if a==1:
        data.accountopen()
    elif a==2:
        data.deposit()
    elif a==3:    
        data.withdraw()
    elif a==4:    
        data.balanceenquiry()
    elif a==5:
        break