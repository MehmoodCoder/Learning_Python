# filter():

numbers = [1, 2, 3, 4, 5, 6]

def is_even(n):
    return n % 2 == 0


result = filter(is_even, numbers)

print(list(result))

# 2.

names = ["Ali","Abdullah","Salam","Bilal","Haris","Kamar"]

def name_filter(names):
    if names != "Bilal":
        return names
        
print(list(filter(name_filter,names)))        
