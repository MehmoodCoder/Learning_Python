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

print(my_kettle.make)
print(my_kettle.on)
my_kettle.switch()
print(my_kettle.on)
print(my_kettle.power_src)
print(friend_kettle.power_src)

print(f"My kettle is On : {my_kettle.switch()}")

