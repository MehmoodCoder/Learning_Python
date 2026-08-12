# List Comprehension Case 1 :

# 1.

li1 = []
for i in range(1,11):
    li1.append(i)

print(li1) 

# 2.

li2 = [i for i in range(1,11)]
print(li2)

# List comprehension has two parts in case 1
# 1 is "i" called expression
# 2 is "for i in range(1,11)" is loop


# List Comprehension Case 2 :

# 1.

li3 = []

for i in range(1,11):
    li3.append(i**2)

print(li3)    

# 2.

li4 = [i**2 for i in range(1,11)]
print(li4)

# List comprehension has two parts in case 2
# 1 is "i**2" called expression
# 2 is "for i in range(1,11)" is loop


# List Comprehension Case 3 :

# 1.


even_li = []
for i in range(1,11):
    if i % 2 == 0:
        even_li.append(i**2)
print(even_li)        

# 2.

li5 = [i**2 for i in range(1,11) if i % 2 == 0]
print(li5)

# List comprehension has three parts in case 3
# 1 is "i**2" called expression
# 2 is "for i in range(1,11)" is loop
# 3 is "if i % 2 == 0" is condition
