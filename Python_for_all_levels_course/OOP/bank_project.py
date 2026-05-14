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


# 2




