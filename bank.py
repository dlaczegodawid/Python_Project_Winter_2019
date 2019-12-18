
class Customer:
    last_id = 0
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __str__(self):
        return "Customer[{0},{1},{2}]".format(self.customer_id, self.first_name, self.last_name)

class Account:
    last_id = 0
    interest_rate = 0.001
    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.account_id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        self.amount  = amount
        self._balance= self._balance + self.amount
        return self._balance

    def charge(self, amount):
        self.amount  = amount
        return self.deposit(amount)- self.amount

    def calc_interest(self):

        return interest

    def get_balance(self):
        self._balance = self.deposit(self.amount)-self.charge(self.amount2)-self.calc_interest()
        return self._balance

    def __str__(self):
        return "{0}[{1},{2},{3}]".format(self.__class__.__name__, self.account_id, self._balance, self.customer.last_name)


c1 = Customer("Anne","Smith","anne@smith.com")
a1 = Account(c1)
c2 = Customer("John", "Brown","john@brown.com")

a1.charge(2)
a1.deposit(100)


print(a1.get_balance())

