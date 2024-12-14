class bank:

    acno:str

    balance:int

    ac_type:str

    customer_name:str

    def __init__(self,acno,balance,ac_type,customer_name):

        self.acno=acno
        self.balance=balance
        self.ac_type=ac_type
        self.customer_name=customer_name

    def display(self):

        print(self.acno,self.balance,self.ac_type,self.customer_name)


    def deposit(self,d_amount):

        self.balance+=d_amount

        print(f"your account{self.acno} has been credited with amount{d_amount} and avail balace is {self.balance}")

    

    def withdraw(self,w_amount):

        if self.balance<w_amount:

            print("insufficient balance")

        else:

            self.balance-=w_amount

            print(f"your account{self.acno}has been debited amount {w_amount} ,avail balance:{self.balance}")

    def get_balance(self):

        print("your current balance is",self.balance)

customer1=bank(1001,100000,"savings","xav")

customer1.deposit(20000)

customer1.withdraw(100000)

customer1.get_balance()




    


    