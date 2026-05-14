li = [['A','B','C'],['D','E','F'],['G','H','I']]
my_li = []

for i in li:
    if 'G' not in i:
        my_li.append(i)
    else:
        my_li.append("Letter was skiped")

print(my_li)

my_li2 = [letter if 'G' not in letter else "Letter was skiped" for letter in li]

print(my_li2)
