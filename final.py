from abc import ABC, abstractmethod

class Account(ABC):
    accounts=[]
    def __init__(self,name,email,password,type):
        self.name=name
        self.email=email
        self.accountNo = name+email
        self.passW=password
        self.balance = 0
        self.transactionHistory = []
        self.type=type
        self.loan_amount = 0
        self.loan_feature = True
        self.loan_apply = 0
        Account.accounts.append(self)

    
    def changeInfo(self,name):
        self.name=name
        print(f"\n--> Name is changed of {self.accountNo}")

    def loan_approval(self, opinion):
        if opinion == 0:
            self.loan_feature = False
            print("\n--> You have no access to apply for a loan!!!!!\n")
        else:
            self.loan_feature = True
            print("\n--> You can apply for a loan!!!!!\n")
    
    #Overloading of method changeInfo
    def changeInfo(self,name,passW):
        self.name=name
        self.passW=passW
        print(f"\n--> Name and Password are changed of {self.accountNo}")

    def transaction_history(self,text):
        self.transactionHistory.append(text)
    
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")
            self.transaction_history(f'Deposit : ${amount}')
        else:
            print("\n--> Invalid deposit amount")

    def loan(self, amount):
        if self.loan_feature == True and self.loan_apply < 2:
            if amount >= 0:
                self.loan_apply += 1
                self.balance += amount
                self.transaction_history(f'Loan : ${amount}')
        else:
            print("\n--> You have no access to apply for a loan!!!!!\n")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
            self.transaction_history(f'Withdraw : ${amount}')
        else:
            print("\nInvalid withdrawal amount")

    @abstractmethod
    def showInfo(self):
        pass

class Admin:
    def __init__(self,name):
        self.name = name

class SavingsAccount(Account):
    def __init__(self,name,email,password,interestRate):
        super().__init__(name,email,password,"savings")
        self.interestRate = interestRate

    def apply_interest(self):
        interest = self.balance*(self.interestRate/100)
        #msg
        print("\n--> Interest is applied !")
        self.deposit(interest)
    
    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')


class CurrentAccount(Account):
    def __init__(self,name,email,password):
        super().__init__(name,email,password,"current")
        # self.limit=limit
            

    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')


# Main program

currentUser=None


while True:

    if currentUser is None:

        print("1.admin")
        print("2.user")
        print("3.Exit")

        ch = int(input("Enter any option: "))
        if ch == 1:
            nm = input("Enter account name: ")

            if(nm == 'admin'):
                currentUser = Admin(nm)
            else:
                print("\n\n !!.....Please enter correct name....!!\n\n")
        elif ch == 2:
            nm = input("Enter account name: ")
            for account in Account.accounts:
                if account.name == nm:
                    currentUser = account
        elif ch == 3:
            break

    elif currentUser.name == "admin":
        

        print("1.Create new account")
        print("2.Delete any account")
        print("3.see all user accounts list")
        print("4.total balance of the bank")
        print("5.total loan amount")
        print("6.on or off the loan feature")
        print("7.LogOut")

        
        op = int(input("Chose options: "))
        
        if op == 1:
            name=input("Name:")
            em=input("Email:")
            pa=input("Password:")
            a=input("Savings Account or special Account (saving / current ) :")
            if a == 'saving':
                ir=int(input("Interest rate:"))
                currentUser=SavingsAccount(name,em,pa,ir)
            elif a == 'current':
                currentUser=CurrentAccount(name,em,pa)

        elif op == 2:
            am = input("Enter account name :")
            i = 0
            for account in Account.accounts:
                i = i + 1
                if account.name == am:
                    del Account.accounts[i-1]
                    break
        elif op == 3:
            for account in Account.accounts:
                print(f'Account name: {account.name}')
                print(f'Account Number: {account.accountNo}')
                print(f'Balance : {account.balance}')
                print(f'Account type : {account.type}')
                print('\n ....... Another Account ...\n')
        elif op == 4:
            bl = 0
            for account in Account.accounts:
                account.balance += bl
            print(f'\n Total balance of the bank: {bl}')
        elif op == 5:
            la = 0
            for account in Account.accounts:
                account.balance += la
            print(f'\n Total loan amount of the bank: {la}')
        elif op == 6:
            lf = int(print(("Enter 1 for approval or 0 for not")))
            Account.loan_approval(lf)
        elif op == 7:
            currentUser = None

    else:
        print(f"\nWelcome {currentUser.name} !\n")
        
        # if currentUser.type=="savings":
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Transfer money")
        print("5. Apply Interest")
        print("6. Apply Loan")
        print("7. Transaction History")
        print("8. Logout\n")
        
        op=int(input("Chose Option:"))
        
        if op==1:
            amount=int(input("Enter withdraw amount:"))
            currentUser.withdraw(amount)
            
        elif op==2:
            amount=int(input("Enter deposit amount:"))
            currentUser.deposit(amount)
        
        elif op==3:
            print(f'available balance : {currentUser.balance}')
        
        elif op==4:
            nm = input("Enter account name:")
            flag = False
            for account in Account.accounts:
                if account.name==nm:
                    flag == True
                    p = int(input("Enter amount :"))
                    currentUser.withdraw(p)
                    account.deposit(p)
                    break
            if flag == False:
                print("\n\nAccount does not exist\n\n")

        elif op==5:

            if currentUser.type == 'current':
                print("\n!!!....you can not apply for interest..!!\n")
            else:
                currentUser.apply_interest()

        elif op==6:
            loan = int(input("Amount for loan :"))
            currentUser.loan(loan)
        elif op==7:
            for history in currentUser.transactionHistory:
                print(history)

        elif op==8:
            currentUser=None
        else:
            print("Invalid Option")



                    


















# while(True):
#     if currentUser==None:
#         print("\n--> No user logged in !")
#         ch=input("\n--> Register/Login (R/L) : ")
#         if ch=="R":
#             name=input("Name:")
#             no=input("Account Number:")
#             pa=input("Password:")
#             a=input("Savings Account or special Account (sv/sp) :")
#             if a=="sv":
#                 ir=int(input("Interest rate:"))
#                 currentUser=SavingsAccount(name,no,pa,ir)
#             else:
#                 lm=int(input("Overdraft Limit:"))
#                 currentUser=SpecialAccount(name,no,pa,lm)
#         else:
#             no=int(input("Account Number:"))
#             for account in Account.accounts:
                
#                 if account.accountNo==no:
#                     currentUser=account
#                     break
                
#     else:
#         print(f"\nWelcome {currentUser.name} !\n")
        
#         if currentUser.type=="savings":
            
#             print("1. Withdraw")
#             print("2. Deposit")
#             print("3. Show Info")
#             print("4. change Info")
#             print("5. Apply Interest")
#             print("6. Logout\n")
            
#             op=int(input("Chose Option:"))
            
#             if op==1:
#                 amount=int(input("Enter withdraw amount:"))
#                 currentUser.withdraw(amount)
                
#             elif op==2:
#                 amount=int(input("Enter deposit amount:"))
#                 currentUser.deposit(amount)
            
#             elif op==3:
#                 currentUser.showInfo()
            
#             elif op==4:
#                 print("Homework")
            
#             elif op==5:
#                 currentUser.apply_interest()
            
#             elif op==6:
#                 currentUser=None
#             else:
#                 print("Invalid Option")
        
#         else:
#             print("1. Withdraw")
#             print("2. Deposit")
#             print("3. Show Info")
#             print("4. change Info")
#             print("5. Logout\n")
            
            
#             op=int(input("Chose Option:"))
            
#             if op==1:
#                 amount=int(input("Enter withdraw amount:"))
#                 currentUser.withdraw(amount)
                
#             elif op==2:
#                 amount=int(input("Enter deposit amount:"))
#                 currentUser.deposit(amount)
            
#             elif op==3:
#                 currentUser.showInfo()
            
#             elif op==4:
#                 print("Homework")
            
#             elif op==5:
#                 currentUser=None
            
#             else:
#                 print("Invalid Option")