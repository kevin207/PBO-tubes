import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="banktera"
)

mycursor = mydb.cursor()

class Customers:
    def __init__(self,customer_id,name,address,phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone

class Accounts(Customers):
    def __init__(self, customer_id, account_id,type,balance):
        super().__init__(customer_id)
        self.account_id = account_id
        self.type = type
        self.balance = balance

class CheckingAccounts(Accounts):
    def __init__(self, customer_id, account_id, type, balance,credit_limit,fee):
        super().__init__(customer_id, account_id, type, balance)
        self.credit_limit = credit_limit
        self.fee = fee

class SavingAccounts(Accounts):
    def __init__(self, customer_id, account_id, type, balance,interest_rate):
        super().__init__(customer_id, account_id, type, balance)
        self.interest_rate = interest_rate

class LoanAccounts(Accounts):
    def __init__(self, customer_id, account_id, type, balance,principal_amount,interest_rate,loan_duration):
        super().__init__(customer_id, account_id, type, balance)
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_duration = loan_duration

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
                print("\n")
                Option = int(input("New Customer?\n1. Yes | 2. No\n>"))
                if Option == 1:
                    loop = False
                    pass
                elif Option == 2:
                    loop = False
                    pass
                else:
                    print("Wrong input")
            except ValueError:
                    print("Please input Integer")

    def New_Customer():
        pass

class Admin_Interface:
    def User_Admin():
        pass

def Login():
    loop = True
    while loop:
        try:
            User_type = int(input("Choose User type:\n1. Customer | 2. Admin\n>"))
            if User_type == 1:
                Customers_Interface.User_Customer()
                loop = False
            elif User_type == 2:
                loop = False
                Admin_Interface.User_Admin()
            else:
                print("Wrong input")
        except ValueError:
            print("Please input Integer")

Login()
