class kettle():
    power_src = "DC"
    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False
    def switch(self):
        self.on = True
        return self.on

my_kettle = kettle("iron",450)
friend_kettle = kettle("iron",600)


my_kettle.switch()
print(kettle.__dict__)
print(my_kettle.__dict__)
print(friend_kettle.__dict__)
print("X"*61)
my_kettle.model = "2026"
print(kettle.__dict__)
print(my_kettle.__dict__)
print(friend_kettle.__dict__)
print("X"*61)
kettle.power_src = "Solar"
print(kettle.__dict__)
print(my_kettle.__dict__)
print(friend_kettle.__dict__)
print(my_kettle.power_src)
print(friend_kettle.power_src)
print("X"*61)
my_kettle.power_src = "Battary"
friend_kettle.power_src = "Steam"
print(kettle.__dict__)
print(my_kettle.__dict__)
print(friend_kettle.__dict__)
print(my_kettle.power_src)
print(friend_kettle.power_src)

