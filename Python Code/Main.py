from codecs import lookup
import mysql.connector
import random
import os

#Inisilasi
clear = lambda: os.system('cls')
pause = lambda: os.system('pause')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="banktera"
)

mycursor = mydb.cursor()

class Customers:
    def __init__(self,customer_id,name,address,email,phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
    
    def insert_data(self):
        order = f'insert into customers values (\'{self.customer_id}\',\'{self.name}\',\'{self.address}\',\'{self.phone}\',\'{self.email}\')'
        mycursor.execute(order)
        mydb.commit()
        print("\nNew Customer has been created")

class Accounts():
    def __init__(self, customer_id, account_id,type,balance):
        self.customer_id = customer_id
        self.account_id = account_id
        self.type = type
        self.balance = balance

    def insert_data(self):
        order = f'insert into accounts values (\'{self.account_id}\',\'{self.customer_id}\',\'{self.type}\',\'{self.balance}\')'
        mycursor.execute(order)
        mydb.commit()
        print("Account has been created")

class CheckingAccounts(Accounts):
    def __init__(self, customer_id, account_id, type, balance,credit_limit,fee):
        super().__init__(customer_id, account_id, type, balance)
        self.credit_limit = credit_limit
        self.fee = fee

    def insert_data(self):
        order = f'insert into accounts values (\'{self.account_id}\',\'{self.customer_id}\',\'{self.type}\',\'{self.balance}\')'
        mycursor.execute(order)
        mydb.commit()
        print("\nChecking Account has been created")

class SavingAccounts(Accounts):
    def __init__(self, customer_id, account_id, type, balance,interest_rate):
        super().__init__(customer_id, account_id, type, balance)
        self.interest_rate = interest_rate

    def insert_data(self):
        order = f'insert into accounts values (\'{self.account_id}\',\'{self.customer_id}\',\'{self.type}\',\'{self.balance}\')'
        mycursor.execute(order)
        mydb.commit()
        print("\nSaving Account has been created")

class LoanAccounts(Accounts):
    def __init__(self, customer_id, account_id, type, balance,principal_amount,interest_rate,loan_duration):
        super().__init__(customer_id, account_id, type, balance)
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_duration = loan_duration

    def insert_data(self):
        order = f'insert into accounts values (\'{self.account_id}\',\'{self.customer_id}\',\'{self.type}\',\'{self.balance}\')'
        mycursor.execute(order)
        mydb.commit()
        print("\nLoan Account has been created")

class AccountTransactions(Accounts):
    def __init__(self, account_id,date,trans_type,amount):
        super().__init__(account_id)
        self.date = date
        self.trans_type = trans_type
        self.amount =amount

class Customers_Interface:
    def User_Customer():
        loop = True
        while loop:
            try:
                Option = int(input("New Customer?\n1. Yes | 2. No\n>"))
                if Option == 1:
                    loop = False
                    clear()
                    Customers_Interface.New_Customer()
                elif Option == 2:
                    loop = False
                    clear()
                    Customers_Interface.Existing_Customer()
                else:
                    print("Wrong input")
                    pause()
                    clear()
            except ValueError:
                    print("Please input Integer")
                    pause()
                    clear()

    def New_Customer():
        print("|Create New Customer|")
        print("Input the following data")
        mycursor.execute("Select Customer_ID from customers")
        result = mycursor.fetchall()
        loop = True
        while loop:
            temp_1 = "CS" + str(random.randint(101000,101999))
            if temp_1 in result:
                pass
            elif not temp_1 in result:
                loop = False
        print(temp_1)
        temp_2 = input("Name : ")
        temp_3 = input("Address : ")
        temp_4 = input("Email : ")
        temp_5 = input("Phone : ")
        customer = Customers(temp_1,temp_2,temp_3,temp_4,temp_5)
        customer.insert_data()
        print("You will be directed to Login Page")
        pause()
        clear()
        Customers_Interface.Existing_Customer()

    def Existing_Customer():
        loop = True
        while loop:
            print("|Customer Login|")
            print("Input the following data")
            temp_1 = input("Customer ID : ")
            #Verify
            Verify = None
            mycursor.execute(f'SELECT Customer_ID FROM Customers where Customer_ID = (\'{temp_1}\')')
            result = mycursor.fetchall()
            for x in result:
                Verify = x[0]
            if not Verify == None:
                print("\nLogin Success")
                loop = False
                #Fetch Name
                mycursor.execute(f'SELECT Name FROM Customers where Customer_ID = (\'{temp_1}\')')
                result = mycursor.fetchall()
                for x in result:
                    temp_2 = x[0]
                #Fetch address
                mycursor.execute(f'SELECT address FROM Customers where Customer_ID = (\'{temp_1}\')')
                result = mycursor.fetchall()
                for x in result:
                    temp_3 = x[0]
                #Fetch Email
                mycursor.execute(f'SELECT Email FROM Customers where Customer_ID = (\'{temp_1}\')')
                result = mycursor.fetchall()
                for x in result:
                    temp_4 = x[0]
                #Fetch Phone
                mycursor.execute(f'SELECT Phone FROM Customers where Customer_ID = (\'{temp_1}\')')
                result = mycursor.fetchall()
                for x in result:
                    temp_5 = x[0]
                customer = Customers(temp_1,temp_2,temp_3,temp_4,temp_5)
                print("You will be directed to the Main Menu")
                pause()
                clear()
                Customers_Interface.Menu(customer)

            else:
                print("Cannot find the designated Customer ID")
                pause()
                clear()

    def New_Account(customer):
        loop = True
        print("|Create New Account|")
        print("Input the following data")
        temp_2 = customer.customer_id
        while loop:
            try:
                Account_option = int(input("Choose Account Type\n1.Checking | 2.Saving | 3.Loan\n>"))
                if Account_option == 1:
                    loop = False
                    temp_3 = "Checking"
                elif Account_option == 2:
                    loop = False
                    temp_3 = "Saving"
                elif Account_option == 3:
                    loop = False
                    temp_3 = "Loan"
                else:
                    print("Wrong input")
            except ValueError:
                print("Please input integer")
        
        temp_4 = ""
        if Account_option == 1:
            mycursor.execute("Select Account_ID from accounts")
            result = mycursor.fetchall()
            # temp_1 = "ACCA" + str(random.randint(1000,1999))
            loop = True
            while loop:
                temp_1 = "ACCA" + str(random.randint(1000,1999))
                if temp_1 in result:
                    pass
                elif not temp_1 in result:
                    loop = False
            account = CheckingAccounts(temp_2,temp_1,temp_3,temp_4,None,None)
            account.insert_data()
            pause()
            clear()
            Customers_Interface.Menu(customer)
        elif Account_option == 2:
            mycursor.execute("Select Account_ID from accounts")
            result = mycursor.fetchall()
            # temp_1 = "ACSA" + str(random.randint(1000,1999))
            loop = True
            while loop:
                temp_1 = "ACSA" + str(random.randint(1000,1999))
                if temp_1 in result:
                    pass
                elif not temp_1 in result:
                    loop = False
            account = SavingAccounts(temp_2,temp_1,temp_3,temp_4,None)
            account.insert_data()
            pause()
            clear()
            Customers_Interface.Menu(customer)
        elif Account_option == 3:
            mycursor.execute("Select Account_ID from accounts")
            result = mycursor.fetchall()
            # temp_1 = "ACLA" + str(random.randint(1000,1999))
            loop = True
            while loop:
                temp_1 = "ACCA" + str(random.randint(1000,1999))
                if temp_1 in result:
                    pass
                elif not temp_1 in result:
                    loop = False
            account = LoanAccounts(temp_2,temp_1,temp_3,temp_4,None,None,None)
            account.insert_data()
            pause()
            clear()
            Customers_Interface.Menu(customer)
        else:
            print("something went wrong")
        
    def Existing_Account():
        loop = True
        while loop:
            print("\nInput the following data")
            temp_1 = input("Account ID : ")
            #Verify
            Verify = None
            mycursor.execute(f'SELECT Account_ID FROM Accounts where Account_ID = (\'{temp_1}\')')
            result = mycursor.fetchall()
            for x in result:
                Verify = x[0]
            if not Verify == None:
                print("Login Success")
                loop = False
                #Fetch Customer ID
                mycursor.execute(f'SELECT Customer_ID FROM Accounts where Account_ID = (\'{temp_1}\')')
                result = mycursor.fetchall()
                for x in result:
                    temp_2 = x[0]
                #Fetch Account Type
                mycursor.execute(f'SELECT type FROM Accounts where Account_ID = (\'{temp_1}\')')
                result = mycursor.fetchall()
                for x in result:
                    temp_3 = x[0]
                #Fetch Balance
                mycursor.execute(f'SELECT Balance FROM Accounts where Account_ID = (\'{temp_1}\')')
                result = mycursor.fetchall()
                for x in result:
                    temp_4 = x[0]
                if temp_3 == "Checking":
                    account = CheckingAccounts(temp_2,temp_1,temp_3,temp_4,None,None)
                elif temp_3 == "Saving":
                    account = SavingAccounts(temp_2,temp_1,temp_3,temp_4,None)
                elif temp_3 == "Loan":
                    account = LoanAccounts(temp_2,temp_1,temp_3,temp_4,None,None,None)
            else:
                print("Cannot find the designated Account ID")

    def Menu(customer):
        print("|Menu|")
        loop = True
        while loop:
            try:
                Option = int(input("Choose the following option\n1. Access Account | 2. Create Account | 3. Log Out\n>"))
                if Option == 1:
                    loop = False
                    clear()
                    print("Access Account")
                elif Option == 2:
                    loop = False
                    clear()
                    Customers_Interface.New_Account(customer)
                
                elif Option == 3:
                    loop = False
                    clear()
                    customer = Customers(None,None,None,None,None)
                    print("You will be directed to the Login Page")
                    pause()
                    clear()
                    Login()
                else:
                    print("Wrong input")
                    pause()
                    clear()
            except ValueError:
                    print("Please input Integer")
                    pause()
                    clear()

    def Account_Access(customer):
        pass
    
class Admin_Interface:
    def User_Admin():
        loop = True
        while loop:
            print("|Admin Login|")
            print("Input the following data")
            temp_1 = input("Admin ID : ")
            temp_2 = input("Password : ")
            #Verify
            Verify_ID = None
            Verify_Pass = None
            mycursor.execute(f'SELECT Admin_ID FROM admin where Admin_ID = (\'{temp_1}\')')
            result = mycursor.fetchall()
            for x in result:
                Verify_ID = x[0]
            mycursor.execute(f'SELECT Password FROM admin where Admin_ID = (\'{temp_1}\')')
            result = mycursor.fetchall()
            for x in result:
                Verify_Pass = x[0]
            if not Verify_ID == None and Verify_Pass == temp_2:
                print("\nLogin Success")
                loop = False
                print("You will be directed to the Main Menu")
                pause()
                clear()
                Admin_Interface.Menu()
            elif Verify_ID == None:
                print("\nWrong Admin ID!")
                pause()
                clear()
            elif not Verify_Pass == temp_2:
                print("\nWrong Password!")
                pause()
                clear()
                
    def Menu():
        print("|Menu|")
        loop = True
        while loop:
            try:
                option = int(input("Choose the following option:\n1. View All Customers Balance | 2. Delete Customer Account |3. Logout\n>"))
                if option == 1:
                    clear()
                    print("View Customer Balance")
                    clear()
                    loop = False
                elif option == 2:
                    clear()
                    pass
                    loop = False
                elif option == 3:
                    clear()
                    print("You will be directed to the Login Page")
                    pause()
                    clear()
                    loop = False
                    Login()
                else:
                    print("Wrong input")
            except ValueError:
                print("Please input Integer")

def Login():
    loop = True
    while loop:
        try:
            User_type = int(input("Choose User type:\n1. Customer | 2. Admin\n>"))
            if User_type == 1:
                clear()
                Customers_Interface.User_Customer()
                loop = False
            elif User_type == 2:
                clear()
                loop = False
                Admin_Interface.User_Admin()
            else:
                print("Wrong input")
        except ValueError:
            print("Please input Integer")

if __name__ == "__main__":
    clear()
    Login()

