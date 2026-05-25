# Python is a programming language. 









# Concepts of Python 
"""
import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
print(str)

age = 100
if age == 100:
   print('age is 100')
else:
    print(f"age is {age}")
for i in range(5):
    print(age, end=" ")
"""
#  ≥

'''
S#,Salary Range,Allowance,Text deduction
1,"0 - 500",10 %,0 %
2,">500 - 1000",9 %,1 %
3,">1000 - 1500",8 %,2 %
4,">1500 - 2000",7 %,3 %
5,">2000 - 3000",6 %,4 %
6,"> 3000",5 %,5 %
'''
"""  
A means Allowance 
T means Tax deduction 
Gs means Gross Salary 
S means Salary 

S = int( input  ("enter your salary : "))
if S >= 0 and S <= 500:
      A = S * 0.10
      T = S * 0.0
      Gs = A + S - T
      print("your salary is : ",Gs)
elif S > 500 and S <= 1000:
      A = S * 0.09
      T = S * 0.01 
      Gs = A + S - T
      print("your salary is : ",Gs)
elif S > 1000 and S <= 1500:
      A = S * 0.08
      T = S * 0.02 
      Gs = A + S - T
      print ("your salary is : ",Gs) 
elif S > 1500 and S <= 2000:
      A = S * 0.07
      T = S * 0.03 
      Gs = A + S - T
      print ("your salary is : ",Gs)   
elif S > 2000 and S <= 3000:
      A = S * 0.06
      T = S * 0.04
      Gs = A + S - T
      print ("your salary is : ",Gs) 
elif S > 3000:
      A = S * 0.05
      T = S * 0.05
      Gs = A + S - T
      print ("your salary is : ",Gs)       
else:
      print("Invalid input")   
"""

"""

print("2" + "3" * 2 )
# 233

"""

"""
if 10 == 10.0:
    print("same")
else : 
    print("different")
    """
    
"""
i = 1
while i < 0:
    print(i)
else:
    print("Done")    
    """
    
"""   
a = [1,2,3]    
b=a
a=a+[4]
print(b)
"""
"""

s = {1,2,3,2}
print(s)

"""
"""
n = "Python"
if n == "Java" or "HTML":
    print("login successfully")
else:
    print("Authorization")    
    
    
"""  
"""  
x = 3
if x % 2 == False:
    print("odd")   
elif x % 2:
    print("even")    
else:
    print("none")    
"""    
"""
x = 10

if x > 5:
    x = x * 2
    if x > 30:
        x = x - 5
  
print(x)
"""
"""
food = "pizza"
food.replace("z","s")
print(food)
"""
"""
a = "3"
a*=2
print(int(a)+5)
"""
"""
x = 0

if x == False:
    print("A")
if x is False:
    print("B")
else:
    print("C")
"""
"""
password = "123"
if password == 123:
    print("login successfully")
else:
    print("Incorrect password!")
"""
"""
x = "40"
y = 8
print(x+y)
"""
"""
x = 5

if x > 2:
    print("A")
elif x > 3:
    print("B")
elif x > 4:
    print("C")
else:
    print("D")
"""
"""
a = int("1a1",15)
print(a)
"""
"""
breakfast1 = ["apple","banana","cherry"]
breakfast2 = ["banana", "cherry","date"]

print(breakfast1 - breakfast2)
"""
"""   

x = int("10.5")
print(x)
"""
"""
friend     = "busy"
if friend:
    print("not replied")
else:
    print("seen only")    
"""    
"""
s = "hello"    
t = s
s = s.upper()   
print(t) 
"""   
"""    
artist = ["Artist1","Artist2","Artist3"]    
print(artist[1])   
""" 
"""
a = "10"
b = 10
print(a == str(b))
"""
"""
x = 5
y = x
x += 1
print(x,y)    
"""
"""
s = "python"
s = s * 5
print(s[7])
"""
"""
a = "Python"
b = "Py"

print(a is b + "thon")
"""

"""
a = "Good"+"Evening"

if a == "Good Evening":
    print("hii")
else:
    print("byee")
"""
"""
a = None
b = True
c = False
print(a == c,a is c)
"""
"""
x = 10
y = 20
x,y=y,x
print(x, y)
"""
"""
x = 5
if x > 3:
    pass
else:
    print("Fail")   
print("Done")
"""
"""
a = [1,2,3]
a.extend([4,5])
print(len(a))
"""
"""
for i in range(3):
    print(i)
    i = 10
"""    
"""
a = [[]]*2
a[0].append(7)
print(len(a[1]))
"""
"""
a = 0.1 + 0.2
#print(a)
b = 0.3
print(a == b)
"""
"""
a = [1,2,3]
b = a#Reference 
c = a[:] # Shallow copy 
b[0] = 100
c[1] = 200
print(a)
#print(b)
#print(c)
"""
"""
score = 90
if score > 90:
    print("Very high")
elif score > 75 and score < 90:
    print("High")
elif score == 100:
    print("Very very High")
else:
    print("Low")
"""
"""
"Python programming". title()
"""
"""
list = [1,2,3]
list.pop(1)
print(list)
"""
"""
a = [1,2]
b = a * 2
b[0] = 99
print(a)
print(b,a)
"""
"""
s = "python"
print(s[::2])# is ka mutlab ha ke start se end tak read karo lekin 2 2 miss kar k3
"""
"""
a = [10,20,30,40,50,60,70]
print(a[:-3])# remove 3 from last 
"""
"""
x = 23
if x * 2 == 46:
    print('false')
"""
"""
x = [1,2,3]
x.append([4,5])
#print(x)
print(len(x))
"""
"""
x = 7
y = 3
if not x > y:
    print(x)
"""
"""
a = "10"
b = "2"
print(a > b)
"""
"""
a = "Python"
print(a[-1:-4:-1])#cut -1 place character only
"""
"""
a = "123"
b= int(a)
print(b+2)
"""
"""
a = [10,20,30]
b = a[1]
a[1] = 99
print(b)
#print(a) as a test
"""
"""
a = [1,2, [3,4]]
a[2].append(5)
print(a)
"""
"""
a = "Python"
print(a[10])
"""
"""
if 10 == 10.0:
    print("same")
else:
    print("different")
"""
# Password Generator 
"""
import string, random 

all_chars = string.ascii_letters + string.digits + string.punctuation
#print(all_chars)
Password = ''.join(random.choices(all_chars, k = 10))
print(Password)
"""
# important interview question 
"""
name = ["Ali","Zayam", "Anas","Haroon"]
marks = [455,544,345,543]

for n,m in zip(name,marks):
    print(n,m)
"""
"""
for i in range(2,10,3):# also count the no which execute peints like 2
    print(i)
"""
"""
x = 2
y = "2"

if x == y:
    print("same")
else:
    print(x+y)
"""
"""
s = "MOHAN"
for i in s :
    print(i)
"""
"""
names = ["faizo","faizan"] 
names.append(names)
#print(names) list under list 
print("\n")
print(len(names))
"""
"""
x = [10,20,30]
x[1] = x[1] + x[0]
print(sum(x))
"""
"""
age = 18
text = "Age : "
print(text + age)
"""
"""
cart = ["shirts","shoes","bags"]
for i in cart :
    cart.remove(i)
print(cart)
"""
"""
user = "mh56"
password = 56
if user and password:
    print("welcome")
else:
    print("sometings wents wrong !")    
"""
"""
s = "hi"
print(s*3 + "!")
"""
"""
for i in range(3):
    if i == 5:
        break 
    else :
        print("done")  
"""
"""
table = 2

for i in range(1,6):
    print(table*i)
"""
"""    
x = 1

if x==1:
    print("1")
elif x is True:
    print("2")
elif x:
    print("3")    
else:
    print("4")
"""
"""
text = "Apple"
text.lower()
text.replace("p","b")# not assign to text 
print(text)
"""
# write first non repeating char in string
"""
s = "Hello World , hi"

for i in s:
    if s.count(i) == 1:
        print(i)
        break 
"""
"""
x = [10,20,30]
x.append((40,50,60))
#print(x)
print(len(x))
"""
"""
s = "python"
s[0] = "P"
print(s)
"""
"""
x = [0] * 3
x[0] = 1
print(x)
"""
"""
a = "2"
b = "10"
print(a>b,a+b)#(Alphabetical order) 
"""
"""
no = [2,4,6,8]
total = 0

for i in no :
    total += i//2
    print(total)
"""

"""
x = "A"

if x * 2:
    if x * 0:
        print("if")
    else:
        print("else")    
"""
"""
x=["a",["b","c"]]
x[1] += ["d"]
print(x)
"""
"""
x = "10"

if 10 == x:
    print("A")
else:
    print(x*2)
"""
"""
no = [10,20]
no.append(no[-1]+5)
print(no)
"""
"""
a = [1,2]
b = [3,4]
print(a+b)
"""
"""
x = [1,2,3,4,5]
for i in x:
    if i == 3:
        x.remove(i)
print(x)
"""
"""
no = [1,2,3]
print(no(1))
"""
"""
x = [1,2,3]
y = x
y.append(4)
print(x)#Object Referencing
"""
"""
x1 = "a"
y1 = 5 
r = x1*y1
print(len(r))
"""
"""
data = [1,2,3]
x = data
x.append(4)
data += [5]
print(len(x),len(data))
"""
"""
x = "pizza"
x = x.replace("z","s")
print(x)
"""

# Task 1

"""
def cal_bill(amount):
    total = 0
    for i in amount:
        total += i        
    if total >= 1000:
        price_after_discount = total - (total * 0.10)
        return round(price_after_discount)
    else:
        return total 
        
prices = input("Please enter the prices separated by commas (e.g., 100,200,300): ").split(",")
prices = [int(i) for i in prices] # (int(i) for i in prices) type generator 

print(f"Total bill is {cal_bill(prices)}")
"""
"""
names = ["Mehmood", "Ali", "Hassan", "Ahmed"]

names = names[::-1]
print(names)
"""    
"""
names = ["Mehmood", "Ali", "Hassan", "Ahmed"]

print(names[1:3])
"""
"""
x = [1,0]
result1 = any(x)
result2 = all(x)
print(result1) 
print(result2) 
"""
"""
x = [1, 2, 3, 4,"ali"]
total = sum(x)
print(total) 
"""
"""
x = ["a","b"]
smallest = min(x)
largest = max(x)
print(smallest) 
print(largest)
"""
"""
s = "Apple"
s.lower()
s.replace("p","b")
print(s)
"""
"""
x = 10
print(x == 5 or 10)
"""
#how do you check 'apple' is exist in list
"""
fruits = ["apple", "banana","mango","orange","Apple", "apple"]
count = (fruits.count("apple"))
if count > 0:
    print(f"'apple' is {count} times exist in list")
else:
    print("'apple' is not exist")
"""
# How to print list without loop 
"""
fruits = ["apple", "banana","mango","orange","Apple", "apple"]
print(fruits)# this is different from 
print(*fruits, sep = "\n")
"""
"""
m = ["Mehmood", "Ahmed", "Ali"]
print(m[-2+1])
"""
"""
x = ([1,2,3])
#x[0].append(4) error write instead 
x.append(4)
print(x)
"""

# merge the list without using loop 
"""
name = ["Mehmood", "Ahmed", "Ali"]
bed = ["1","2","3"]
fee = ['paid','paid','unpaid']

all_details = list(zip(name, bed, fee))
print(all_details)
"""
"""
x = []
#print(x)
if x:
    print('Hulk')
else:
    print('Spider-Man')
"""
"""
x = [1,2,3]
for i in x:
    x.append(i)
print(len(x))
"""
"""
print = "freefire"
print(print)
"""
"""
a = "10"
b = float(a)
print(int(b) + 2)
"""
"""
# if values are equal both sides
#a,b,c = 1,2,3
# but if both sides values are not equal 
#a,b,c = 1,2,3,4,5,6,7,8,9,10
# to fix this issue we write as
a,*b,c = 1,2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)
"""
"""
x = [1,2,3]
y = x
z = x.copy()
x.append(4)
print(y)
print(z)
"""
# Encryption and Decryption 
"""
message = input('Enter your message : ')[::-1]
print(f'hacker reads {message}')
print(f'My friend reads {message[::-1]}')
"""
"""
print("hello" * 0)
"""
"""
x = [1,2,3]
print(x*2)
print([x] * 2)
print(x)
"""
"""
x = True 
y = False 

if x == (not y):
    print("A")
elif not x == y:
    print("B")
elif not(x == y):
    print("C")
else:
    print("D")
"""
"""
x = "A"
y = 5
print(len(x*y))
"""
"""
x = "Uga"
y = "idag"
r = x + y[::-1][1:]
print(r)
"""
"""
import sys
import time

def print_lyrics():
    lyrics = [
        "Sambhaal ke rakha wo phool mera tu",
        "Meri shayari mein zaroor raha tu",
        "Jo aankhon mein pyaari si duniya basaayi",
        "Wo duniya bhi tha tu, wo lamha bhi tha tu",
        "Haan, lagte hain mujhko ye kisse sataane",
        "Deta na dil mera tujhko bhulaane",
        "Adhoore se vaade, adhoori si raatein",
        "Ab hisse mein daakhil mere bas wo yaadein"
    ]

    delays = [0.7, 0.7, 0.4, 0.5, 0.5, 0.7, 0.7, 1.0]

    print("Finding Her: \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(delays[i])

#print_lyrics()
"""
"""
s = "Pineapple"
s = s.lower()
s.split('e')
print(s)
"""
"""
s = "dog"
if s:
    print(s == "cat")
else:
    print("empty")
"""
"""
# Reference 

x = [[]] * 3
print(x)
x[0].append('a')
x[1].append('b')
x[2].append('c')
print(x)
"""
"""
x = int(input('Enter a number : '))
for i in range(1,11):
    print(f'{x} x {i} = {x*i}')
"""
"""
store = ['Green shirt','Red shirt' 'Black shirt','Blue shirt', 'Yellow shirt']

for shirt in store:
    if shirt == "Green shirt":
        print(f'This shirt I need , {shirt}')
"""
"""
# Walrus Operator 

while (data.lower() := input('Enter exit to break the loop : ')) != "exit":
    print('I am good')
else:
    print('Break loop')
"""


