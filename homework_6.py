
#Please extend the Account class located in Bank by adding the history of transactions.
#Entries should be added to the history everytime the "deposit", "charge" or "calc_interest" methods are called and
#should contain the operation type (same as method name), the parameter value (amount), the balance after the operation
#and date and time automatically taken from the operating system.
#You may implement it as just a list of string entries, however, a preferred way would be to create a separate class as
#a template for each Operation entry.
import time
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
        self._translist = []
    def deposit(self, amount):
        if amount>0:
            self._balance += amount

        else:
            raise BankException('Negative amount')

        self._translist.append((self.deposit.__name__, amount, self._balance, time.ctime(time.time())))
    def charge(self, amount):
        if amount < 0:
            raise NegativeAmountException()
        if amount > self._balance:
            raise NotEnoughMoneyException()

        self._balance -= amount


        self._translist.append((self.charge.__name__, amount, self._balance,time.ctime(time.time())))

    def calc_interest(self):
        self._balance += self._balance * self.interest_rate

        self._translist.append((self.calc_interest.__name__, self._balance * self.interest_rate, self._balance,time.ctime(time.time())))
    def get_balance(self):
        return self._balance



    def __str__(self):
        return "{0}[{1},{2},{3}]".format(self.__class__.__name__, self.account_id, self._balance, self.customer.last_name)

    def show_list(self):
        return self._translist


class BankException(Exception):
    pass
class NegativeAmountException(BankException):
    pass
class NotEnoughMoneyException(BankException):
    pass

c1 = Customer("Anne","Smith","anne@smith.com")
a1 = Account(c1)
c2 = Customer("John", "Brown","john@brown.com")
print(c1)
print(a1)
try:
    a1.deposit(20000)
    a1.charge(150)
    a1.deposit(1000)
    a1.calc_interest()
    print(a1.show_list())
except NotEnoughMoneyException as ne:
    print("Not enough money")
    print(ne)
except NegativeAmountException as na:
    print("not enough money")
    print(na)

#print(a1.show_list())

#class Transhist(Account):
#    def __init__(self):
#        self.op_type = __name__
#        self.amount = self.amount
#        self.balance = self.balance
#        self.timestamp = datetime.now()
#    def returnelement(self):
#        return self.op_type, self.amount, self.balance, self.timestamp

