# a variable "var" can be made private by placing 2 underscores "__" in front of the variable:-->"__var" 

from abc import ABC,abstractmethod

class Bankaccount:

    customer_name:str

    mpin:int

    account_type:str

    balance:int

    def __init__(self,customer_name,mpin,account_type,balance):

        self.customer_name=customer_name

        self.__mpin=mpin  #here variable "mpin" is made 'private' using "__mpin"

        self.account_type=account_type

        self.__balance=balance  # balance is also made 'private'

    def get_balance(self):

        print(self.__balance)

    def __str__(self):

        return self.customer_name
    
bankaccount_instance=Bankaccount("xav",2002,"savings",50000)

print(bankaccount_instance)
    
# print(bankaccount_instance.__mpin)
