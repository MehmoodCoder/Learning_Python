# Nested for in List Comprehension

# Normal Way

A = [2,4,6]
B = [1,3,5]
C = []


for i in A:
    for j in B:
        C.append(i*j)
print(C) 

# Comprehension Way

my_li = [i*j for i in A for j in B]
print(my_li)




