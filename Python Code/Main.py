from codecs import lookup
from abc import ABC, abstractmethod
import mysql.connector
import random
import os
from prettytable import PrettyTable
import prettytable

def get_time():
    from datetime import datetime
    now = datetime.now()
    d3 = now.strftime("%Y-%m-%d %H:%M:%S")
    return d3

#Inisilasi
clear = lambda: os.system('cls')
pause = lambda: os.system('pause')
loop = True
while loop:
    try:
        clear()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database ="banktera"
        )

        mycursor = mydb.cursor()
        loop = False
    except :
        print("Can't connect to Database")
        print("Try to restart MySQL Module")
        print("\nRetry?")
        pause()

#Overriding ada pada insert data (Same method and arguments from parents, different function in child) DONE

#Overloading ada pada (Same method but diffrent arguments)
#EXAMPLE:

    #def add_bullet(sprite, start, headto, spead, acceleration):
    #def add_bullet(sprite, script): # For bullets that are controlled by a script
    #def add_bullet(sprite, curve, speed): # for bullets with curved paths
        
class AbstractClass(ABC): #Penerapan Abstract class dengan abstract method insert_data DONE

    def __init__(self,customer_id,name,address,email,phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        super().__init__()

    @abstractmethod 
    def insert_data(self):
        pass
    
class Customers(AbstractClass):
    def __init__(self,customer_id,name,address,email,phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

    def import_customer_id(self):
        return self.customer_id
    
    def insert_data(self): 
        order = f'insert into customers values (\'{self.customer_id}\',\'{self.name}\',\'{self.address}\',\'{self.phone}\',\'{self.email}\')'
        mycursor.execute(order)
        mydb.commit()
        print("\nNew Customer has been created")

class Accounts(AbstractClass):
    def __init__(self, customer_id, account_id,type,balance):
        self.customer_id = customer_id
        self.account_id = account_id
        self.type = type
        self.balance = balance

    def import_account_id(self):
        return self.account_id

    def import_type(self):
        return self.type
    
    def balance_setter(self,input):
        self.balance = input
        
    def balance_getter(self):
        return self.balance
    
    def customer_id_setter(self,input):
        self.customer_id = input

    def account_id_setter(self,input):
        self.account_id = input

    def type_setter(self,input):
        self.type_id = input

    def insert_data(self): #overriding (Parent Class)
        order = f'insert into accounts values (\'{self.account_id}\',\'{self.customer_id}\',\'{self.type}\',\'{self.balance}\')'
        mycursor.execute(order)
        mydb.commit()
        print("Account has been created")
    
    def Deposit():
        pass

    def Withdraw():
        pass

    def Balance_Enquiry():
        pass

class CheckingAccounts(Accounts):
    def __init__(self, customer_id, account_id, type, balance,fee):
        super().__init__(customer_id, account_id, type, balance)
        self.credit_limit = 10000000
        self.fee = fee

    def insert_data(self): #overriding (Child Class)
        order = f'insert into accounts values (\'{self.account_id}\',\'{self.customer_id}\',\'{self.type}\',\'{self.balance}\')'
        mycursor.execute(order)
        mydb.commit()
        print("\nChecking Account has been created")

    def fee_setter(self,input):
        self.fee = abs(input)

    def overdraft(self,input):
        approval = False
        if input > (self.credit_limit*-1):
            #update approval
            approval = True
            return approval
        else:
            #update disapproval
            approval = False
            return approval
        
class SavingAccounts(Accounts):
    def __init__(self, customer_id, account_id, type, balance):
        super().__init__(customer_id, account_id, type, balance)
        self.interest_rate = 10 #10%

    def insert_data(self): #overriding (Child Class)
        order = f'insert into accounts values (\'{self.account_id}\',\'{self.customer_id}\',\'{self.type}\',\'{self.balance}\')'
        mycursor.execute(order)
        mydb.commit()
        print("\nSaving Account has been created")
    
    def monthly_interest(self):
        pass

class LoanAccounts(Accounts):
    def __init__(self, customer_id, account_id, type, balance,principal_amount):
        super().__init__(customer_id, account_id, type, balance)
        self.principal_amount = principal_amount
        self.interest_rate = 10 #10%
        self.loan_duration = 30

    def insert_data(self): #overriding (Child Class)
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
    
    def acc_id_setter(self,input):
        self.account_id= input
    
    def date_setter(self,input):
        self.date = input
    
    def date_getter(self):
        return self.date

    def trans_type_setter(self,input):
        self.trans_type = input
    
    def trans_type_getter(self):
        return self.trans_type

    def amount_setter(self,input):
        self.amount = input

    def amount_getter(self):
        return self.amount

    def save_to_database(self):
        order = f'insert into account_transactions values (\'{self.account_id}\',\'{self.date}\',\'{self.trans_type}\',\'{self.amount}\')'
        mycursor.execute(order)
        mydb.commit()

class Banking_System():
    pass

class Customers_Interface:
    def User_Customer():
        loop = True
        while loop:
            try:
                Option = int(input("New Customer?\n1. Yes | 2. No\n\nAnswer: "))
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
                print("You will be directed to the Customer Menu")
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
                Account_option = int(input("Choose Account Type\n1.Checking | 2.Saving | 3.Loan\n\nAnswer: "))
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
            account = CheckingAccounts(temp_2,temp_1,temp_3,temp_4,None)
            account.insert_data()
            account = CheckingAccounts(None,None,None,None,None)
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
            account = SavingAccounts(temp_2,temp_1,temp_3,temp_4)
            account.insert_data()
            account = CheckingAccounts(None,None,None,None,None)
            pause()
            clear()
            Customers_Interface.Menu(customer)
        elif Account_option == 3:
            mycursor.execute("Select Account_ID from accounts")
            result = mycursor.fetchall()
            # temp_1 = "ACLA" + str(random.randint(1000,1999))
            loop = True
            while loop:
                temp_1 = "ACLA" + str(random.randint(1000,1999))
                if temp_1 in result:
                    pass
                elif not temp_1 in result:
                    loop = False
            account = LoanAccounts(temp_2,temp_1,temp_3,temp_4,None)
            account.insert_data()
            account = LoanAccounts(None,None,None,None,None)
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
        print("|Customer Menu|")
        loop = True
        while loop:
            try:
                Option = int(input("Choose the following option\n1. Access Account | 2. Create Account | 3. Log Out\n\nAnswer: "))
                if Option == 1:
                    loop = False
                    clear()
                    Customers_Interface.Account_Access(customer)
                    
                elif Option == 2:
                    loop = False
                    clear()
                    Customers_Interface.New_Account(customer)
                
                elif Option == 3:
                    clear()
                    customer = Customers(None,None,None,None,None)
                    Logout()
                    
                else:
                    print("Wrong input")
                    pause()
                    clear()
            except ValueError:
                    print("Please input Integer")
                    pause()
                    clear()

    def Saving_Interest(account):
        i=0
        c=[]
        d=[]
        temp_1 = account.import_account_id()
        order = f'SELECT Date_Time FROM account_transactions WHERE Account_ID = \'{temp_1}\''
        mycursor.execute(order)
        result = mycursor.fetchall()
        for x in result:
            a = x[0]
            b = str(a)
            c.append(b[5:7])
            d.append(b[8:10])
        
        print(c)
        pause()

    def Account_Access(customer):
        print("|Choose Account|")
        try:
            i = 0
            j = []
            temp_1 = customer.import_customer_id()
            order = f'SELECT Account_ID,Type FROM accounts WHERE Customer_ID = \'{temp_1}\''
            mycursor.execute(order)
            result = mycursor.fetchall()
            if result:
                temp_2 = PrettyTable(["Account ID", "Account Type"])
                for x in result:
                    temp_2.add_row(x)
                print(temp_2)
                Option = str(input("Input Account ID on the list : "))
                order = f'SELECT Type FROM accounts WHERE Account_ID = \'{Option}\''
                mycursor.execute(order)
                result = mycursor.fetchall()
                for x in result:
                    if x[0] == "Checking":
                        #Fetch Account ID
                        mycursor.execute(f'SELECT Account_ID FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_4 = x[0]
                        #Fetch Customer ID
                        mycursor.execute(f'SELECT Customer_ID FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_3 = x[0]
                        #Fetch Type
                        mycursor.execute(f'SELECT Type FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_5 = x[0]
                        #Fetch Balance
                        mycursor.execute(f'SELECT Balance FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_6 = x[0]
                        account = CheckingAccounts(temp_3,temp_4,temp_5,temp_6,None)
                        Customers_Interface.Account_Menu(account,customer)
                    elif x[0] == "Saving":
                        #Fetch Account ID
                        mycursor.execute(f'SELECT Account_ID FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_4 = x[0]
                        #Fetch Customer ID
                        mycursor.execute(f'SELECT Customer_ID FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_3 = x[0]
                        #Fetch Type
                        mycursor.execute(f'SELECT Type FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_5 = x[0]
                        #Fetch Balance
                        mycursor.execute(f'SELECT Balance FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_6 = x[0]
                        account = SavingAccounts(temp_3,temp_4,temp_5,temp_6)
                        # Customers_Interface.Saving_Interest(account)
                        Customers_Interface.Menu(customer)
                    elif x[0] == "Loan":
                        #Fetch Account ID
                        mycursor.execute(f'SELECT Account_ID FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_4 = x[0]
                        #Fetch Customer ID
                        mycursor.execute(f'SELECT Customer_ID FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_3 = x[0]
                        #Fetch Type
                        mycursor.execute(f'SELECT Type FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_5 = x[0]
                        #Fetch Balance
                        mycursor.execute(f'SELECT Balance FROM accounts where Account_ID = (\'{Option}\')')
                        result = mycursor.fetchall()
                        for x in result:
                            temp_6 = x[0]
                        account = LoanAccounts(temp_3,temp_4,temp_5,temp_6,None)
                        clear()
                        Customers_Interface.Account_Menu(account,customer)
                if not result:
                    print("Account ID not Found!")
                    pause()
                    clear()
                    Customers_Interface.Account_Access(customer)
            else:
                print("\nYou Don't Have Any Account!")
                print("You will be directed to Account Menu")
                pause()
                clear()
                Customers_Interface.Menu(customer)   
        except ValueError:
            Customers_Interface.Account_Access(customer)

    def Deposit(account,customer):
        print("|Deposit|")
        temp_1 = int(input("Value: "))
        if not temp_1 <0:
            temp_2 = account.import_account_id()
            order = f'SELECT Balance FROM accounts WHERE Account_ID = \'{temp_2}\''
            mycursor.execute(order)
            result = mycursor.fetchall()
            for x in result:
                temp_3 = x[0]
            temp_6 = temp_1
            temp_1 = temp_1 + temp_3
            
            mycursor.execute(f'UPDATE accounts set Balance = (\'{temp_1}\') WHERE Account_ID = (\'{temp_2}\')' )
            mydb.commit()

            temp_4 = get_time()
            temp_5 = "Deposit"
            order = f'insert into account_transactions values (\'{temp_2}\',\'{temp_4}\',\'{temp_5}\',\'{temp_6}\')'
            mycursor.execute(order)
            mydb.commit()

            #Set Account Transaction Class
            # acc_trans.balance_setter(temp_1)
            # acc_trans.acc_id_setter(temp_2)
            # acc_trans.date_setter(temp_4)
            # temp_5 = "Deposit"
            # acc_trans.trans_type_setter(temp_5)
            # acc_trans.amount_setter(temp_1)
            # acc_trans.save_to_database()

            print("You will be directed to Account Menu")
            pause()
            clear()
            Customers_Interface.Account_Menu(account,customer)
        else:
            print("You can't input negative value")
            pause()
            clear()
            Customers_Interface.Deposit(account,customer)

    def Withdraw(account,customer):
        print("|Withdraw|")
        transaction = False
        temp_1 = int(input("Value: "))
        temp_1 = abs(temp_1)
        temp_2 = account.import_account_id()

        order = f'SELECT Balance FROM accounts WHERE Account_ID = \'{temp_2}\''
        mycursor.execute(order)
        result = mycursor.fetchall()

        for x in result:
            temp_3 = x[0]

        temp_3 = temp_3 - temp_1
        temp_4 = account.import_type()
        if temp_3<0:
            if temp_4 == "Checking":
                temp_5 = account.overdraft(temp_3)
                if temp_5:
                    account.balance_setter(temp_3)
                    account.fee_setter(temp_3)
                    mycursor.execute(f'UPDATE accounts set Balance = (\'{temp_3}\') WHERE Account_ID = (\'{temp_2}\')')
                    mydb.commit()
                    transaction = True
                elif not temp_5:
                    print("Withdraw Value Exceed Credit Limit!")
                else:
                    print("Error")
            elif temp_4 == "Saving":
                print("\nInsufficient Balance to Withdraw!")

            elif temp_4 == "Loan":
                pass
        elif temp_3 >= 0:
            mycursor.execute(f'UPDATE accounts set Balance = (\'{temp_3}\') WHERE Account_ID = (\'{temp_2}\')')
            mydb.commit()
            transaction = True
        else:
            print("Error")
        if transaction:
            temp_4 = get_time()
            temp_5 = "Withdraw"
            order = f'insert into account_transactions values (\'{temp_2}\',\'{temp_4}\',\'{temp_5}\',\'{temp_1}\')'
            mycursor.execute(order)
            mydb.commit()

        print("You will be directed to Account Menu")
        pause()
        clear()
        Customers_Interface.Account_Menu(account,customer)
    
    def Balance_Enquiry(account,customer):
        print("|Balance|")
        temp_1 = account.import_account_id()
        order = f'SELECT Balance FROM accounts WHERE Account_ID = \'{temp_1}\''
        mycursor.execute(order)
        result = mycursor.fetchall()

        for x in result:
            temp_2 = x[0]
        print("Your Balance : " + str(temp_2))
        print("\nYou will be directed to Account Menu")
        pause()
        clear()
        Customers_Interface.Account_Menu(account,customer)

    def Back_to_Main_Menu(account,customer):
        account.balance_setter(None)
        account.customer_id_setter(None)
        account.account_id_setter(None)
        account.type_setter(None)
        print("You will be directed to Main Menu")
        pause()
        clear()
        Customers_Interface.Menu(customer)
        
    def Transaction_History(account,customer):
        print("|Transaction History|")
        # try:
        temp_1 = account.import_account_id()
        order = f'SELECT * FROM account_transactions WHERE Account_ID = \'{temp_1}\''
        mycursor.execute(order)
        result = mycursor.fetchall()
        temp_2 = PrettyTable(["Account ID", "Date and Time","Transaction Type","Amount"])
        for x in result:
            temp_2.add_row(x)
        print(temp_2)
        print("You will be directed to the Account Menu")
        pause()
        clear()
        Customers_Interface.Account_Menu(account,customer)
        # except:
        #     print("Error")
        #     pause()
        #     clear()

    def Account_Menu(account,customer):
        try:
            clear()
            print("|Account Menu|")
            Option = int(input("Choose the following option\n1. Deposit | 2. Withdraw | 3. Balance Enquiry | 4. Transaction History |5. Back to Main Menu\n\nAnswer: "))
            if Option == 1:
                clear()
                Customers_Interface.Deposit(account,customer)
            elif Option == 2:
                clear()
                Customers_Interface.Withdraw(account,customer)
            elif Option == 3:
                clear()
                Customers_Interface.Balance_Enquiry(account,customer)
            elif Option == 4:
                clear()
                Customers_Interface.Transaction_History(account,customer)
            elif Option == 5:
                Customers_Interface.Back_to_Main_Menu(account,customer)
        except ValueError:
            clear()
            Customers_Interface.Account_Menu(account,customer)
    
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
                print("You will be directed to Admin Menu")
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
                
    def Delete_Account():
        print("|Delete Customer Account|")
        temp_1 = str(input("Input Customer Account\n>"))
        order = f'select Account_ID from accounts where Account_ID  = \'{temp_1}\''
        mycursor.execute(order)
        result = mycursor.fetchall()
        if result:
            order = f'select Account_ID from account_transactions where Account_ID  = \'{temp_1}\''
            mycursor.execute(order)
            result_2 = mycursor.fetchall()
            if result_2:
                order = f'DELETE FROM account_transaction WHERE account_transaction.Account_ID = \'{temp_1}\''
                mycursor.execute(order)
                mydb.commit()
            order = f'DELETE FROM accounts WHERE accounts.Account_ID = \'{temp_1}\''
            mycursor.execute(order)
            mydb.commit()
            clear()
            print("Account Has Been Deleted!\n")
            pause()
            clear()
        else:
            print("Nomor tiket tidak ditemukan!")
            pause()
            clear()
            Admin_Interface.Delete_Account()

    def View_Customer_Data():
        order = f'SELECT customers.customer_id,customers.name,accounts.account_id,accounts.type,accounts.balance FROM customers natural join accounts'
        mycursor.execute(order)
        result = mycursor.fetchall()
        temp_2 = PrettyTable(["Customer ID","Name","Account ID", "Account Type","Balance"])
        for x in result:
            temp_2.add_row(x)
        print(temp_2)
        pause()
        clear()
        Admin_Interface.Menu()
        
    def Menu():
        print("|Admin Menu|")
        loop = True
        while loop:
            try:
                option = int(input("Choose the following option:\n1. View All Customers Balance | 2. Delete Customer Account |3. Logout\n\nAnswer: "))
                if option == 1:
                    clear()
                    Admin_Interface.View_Customer_Data()
                    clear()
                    loop = False
                elif option == 2:
                    clear()
                    Admin_Interface.Delete_Account()
                elif option == 3:
                    Logout()
                else:
                    print("Wrong input")
            except ValueError:
                print("Please input Integer")

def Login():
    loop = True
    while loop:
        try:
            print("|Main Menu|")
            User_type = int(input("Choose User type:\n1. Customer | 2. Admin | 3.Exit \n\nAnswer: "))
            if User_type == 1:
                clear()
                Customers_Interface.User_Customer()
                loop = False
            elif User_type == 2:
                clear()
                loop = False
                Admin_Interface.User_Admin()
            elif User_type == 3:
                print("Program Exited")
                exit()
            else:
                print("Wrong input")
        except ValueError:
            print("Please input Integer")

def Logout():
    clear()
    print("You will be directed to the Main Menu")
    pause()
    clear()
    loop = False
    Login()
    
    
if __name__ == "__main__":
    clear()
    Login()

