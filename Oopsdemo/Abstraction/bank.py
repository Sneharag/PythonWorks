

class Bank:

    def create_acc(self,accno,ac_type):

        self.accno=accno
        self.bank_name="SBI"
        self.__balance=2000
        self.ac_type=ac_type

    def deposit(self,amount):

        self.__balance+=amount
        print(f"your {self.bank_name} accno with {self.accno} has been credited with amount {amount}")

    def withdraw(self,amount):

        if amount>self.__balance:
           
           print("Transaction failed insufficient balance")

        else:
           
            self.__balance-=amount
            print(f"your {self.bank_name} accno with {self.accno} has been debited with amount {amount}")

    def get_balance(self):

        print(f"Your bank balance is {self.__balance}")
    
bank=Bank()

bank.create_acc(1234,"savings")
bank.deposit(1000)
bank.withdraw(500)
# bank.__balance+=2000
bank.get_balance()
