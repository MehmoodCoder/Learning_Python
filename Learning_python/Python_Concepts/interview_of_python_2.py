"""
a = "listen"
b = "silent"

print(sorted(a) == sorted(b))
"""
"""
if " ":
    print('True')
    
else:
    print('False')
"""
"""
x = 1

while x < 6:
    x += 2
    if x == 5:
        break
else:
    x = 100

print(x)
"""
"""
li = [1,2,3,4,5]

for no in li:
    if no == 3:
        break
else:
    print("Else run")
"""
"""
x = [1,2,3]
y = x
y += [4,5]

print(x)
print(y)
"""
'''
print(sorted('banana'))
'''
"""
print(2 ** 3 ** 2)
"""
"""
a = [1,2,3]

print(a * 2 == a + a)
"""
'''
x = [1,2,3]

print(x * 0)
'''
"""
a = ['Ali','Babar']
a += 'Amir'

print(a)
"""
"""
for i in range(5):
    if i == 3:
        break 
else:
    print('Done')
"""
'''
a = bool(input('Enter empty str : '))
# enter zero and check
# enter empty string to check 

print(a)
'''
'''
def f(x, y = 2):
    return x * y

print(f(3, None)) # Type Error 
'''
"""
l = [[1,2], [3,4]]

for i,j in l:
    print(i + j, end = " ")
"""
'''
def append_and_return(val, data = []):
    data.append(val)
    return data
    
x = append_and_return(1)
y = append_and_return(2)
z = append_and_return(3, [])

print(x,y,z)
'''

'''
x = []

x.append(x)

print(x == x[0])

'''
'''
for i in range(3):
    pass
    
print(i)   

'''
"""

for i in range(0,1):
    print(i)
    for j in range(0,0):
        print(j)

"""
"""
def X(a,b = []):
    b.append(a)    
    return b
    
print(X(1))
print(X(2))
"""
"""
if "h":
    pass
else:
    ...
    
print(...)
"""    
'''
print('' == False)
print(0 == False)
print(bool('') == False)

if '':
    print('true')
else:
    print('false')    
'''
'''
def trick():
    try:
        return 1
    finally:
        return 2
        
print(trick())    
'''    