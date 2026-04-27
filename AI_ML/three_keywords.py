i = 1
while i <= 10:

    print(i)
    i += 1
    if i == 9:
        break # 1. break
    elif i == 3:
        continue # 2. continue
    elif i == 5:
        pass # 3. pass
else:
    print("Loop Ends Here") # This will not be executed because of the break statement

# example of pass

# I need this for loop but it causes error without code

for i in range(10):
    pass # it is a solution
else:
    print("For Loop Ends Here")

# example of break

s = "Python is a programming language"

while True:
    if "language" in s:
        print("Found the word 'language' in the string.")
        break
    else:        
        print("The word 'language' is not in the string.")
        break


# example of continue

for i in range(1, 11):
    if i % 2 == 0:
        continue # skip the rest of the loop for even numbers
    print(i) # this will only print odd numbers from 1 to 10


# Why while loop is best than for loop
while True:
    command = input("Please say yes : ")
    if command.lower() == "yes":
        print("Thank you for saying yes!")
        break
    else:
        print("Please try again.")




