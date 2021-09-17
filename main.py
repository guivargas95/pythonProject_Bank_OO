class Bank:
    def __init__(self,account_number, owner, money, limit = 1000):
        self.__account_number = account_number
        self.__owner = owner
        self.__money = money
        self.__limit = limit

    def extract(self):
        print(f"{self.__owner}'s Account\nBalance: U$${self.__money}")

    def draft(self, value):
        if self.__money < value:
            return("Insufficiet funds")
        self.__money -= value
        return(f"Draft complete. Your balance: {self.__money}")


    def deposit(self, value):
        self.__money += value
        return(f"Deposit complete. Your balance: U$${self.__money}")


    def transfer(self,value,account_target):
        if self.__money < value:
            return ("Insufficiet funds")
        self.draft(value)
        account_target.deposit(value)

    def get_money(self):
        return self.__money

    def get_owner(self):
        return self.__owner

    def get_limit(self):
        return self.__limit

    def set_limit(self,value):
        self.__limit = value
