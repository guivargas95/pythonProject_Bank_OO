class Account:

    bank_code = "001" """We can substitute an static method with this"""

    def __init__(self, account_number, owner, money, limit=1000):
        self.__account_number = account_number
        self.__owner = owner
        self.__money = money
        self.__limit = limit

    def extract(self):
        print(f"{self.__owner}'s Account\nBalance: U$${self.__money}")

    def draft(self, value):
        if self.__authorize_draft(value):
            self.__money -= value
            return f"Draft complete. Your balance: {self.__money}"
        else:
            return "Insufficient funds"

    def deposit(self, value):
        self.__money += value
        return f"Deposit complete. Your balance: U$${self.__money}"

    def transfer(self, value, account_target):
        if self.__authorize_draft(value):
            self.draft(value)
            account_target.deposit(value)
        else:
            return "Insufficient funds"

    def __authorize_draft(self, value):
        true_limit = self.__money + self.limit
        return value <= true_limit

    @property
    def money(self):
        return self.__money

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value

    @staticmethod
    def bank_code_method():
        return "001"
