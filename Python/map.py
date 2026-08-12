# map
l = [1,2,3] # data

def adder_map(l):
    return l+1

print(list(map(adder_map,l)))    

# Exercise :

li = [1,2,3] # data

def one_adder(li):
    new_li = []
    for i in li:
        new_li.append(i + 1)
    return new_li   


print(one_adder(li)) # process

