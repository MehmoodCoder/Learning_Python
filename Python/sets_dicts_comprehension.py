# sets/dicts comprehension:

# sets 

set1 = {i for i in range(1,11)}
print(set1)

# dicts

dict1 = {
    "x":1,
    "y":6,
    "z":2
}

dict2 = {key : value ** 2 for key , value in dict1.items()}
print(dict2)

