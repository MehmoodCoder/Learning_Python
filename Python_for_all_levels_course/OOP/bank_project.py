# Khali Bank Ltd

class bank():
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print("Account Successfully Created")
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"You deposite {amount}")
            self.show()
    def widraw(self,amount):
        if amount > 0:
            self.balance -= amount 
            print(f"You widraw {amount}")
            self.show()
            
            
    def show(self):
        print(f"{self.name} Balance = {self.balance}")
        
Mehmood = bank("Mehmood",100000000)
Mehmood.deposite(12000)
# Mehmood.show()
Mehmood.widraw(12000)
# Mehmood.show()

Ali = bank("Ali",89000)
Ali.deposite(5000)
# Failed here
Ali.widraw(100000)
# Ali.show()
print("X"*61)

# 2


class bank():
    
    @staticmethod
    def greet(self):
        greet = f"Hello Welcome back {self.name} !"
        return greet
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print("Account Successfully Created")
    def deposite(self,amount):
        if amount > 0:
            print(bank.greet(self))
            self.balance += amount
            print(f"You deposite {amount}")
            self.show()
    def widraw(self,amount):
        if amount > 0:
            if self.balance > 0:
                if amount <= self.balance:
                    print(bank.greet(self))
                    self.balance -= amount 
                    print(f"You widraw {amount}")
                    self.show()
                else:
                    print(f"{self.name} widraw {amount}.But your balance is {self.balance} !")
    def show(self):
        print(f"{self.name} Balance = {self.balance}")
        
Mehmood = bank("Mehmood",100000000)
Mehmood.deposite(12000)
Mehmood.widraw(12000)

Ali = bank("Ali",90000)
Ali.deposite(5000)
Ali.widraw(100000)


