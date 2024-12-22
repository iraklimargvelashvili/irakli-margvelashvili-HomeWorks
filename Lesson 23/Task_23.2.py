import sys
sys.stdout.reconfigure(encoding='utf-8')

class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("საკმარისი თანხა არ არის.")
        else :
            self._balance -= amount
            print(f"თქვენს ანგარიშზე დარჩა: {self._balance}")

    def get_balance(self):
        return self._balance

account = BankAccount(100)

account.deposit(50)

account.withdraw(30)

account.withdraw(200)

print(f"მიმდინარე ბალანსი: {account.get_balance()}")
