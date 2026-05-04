# Normal :

# def returner(name):
#     return f"Hello {name}!"


# name = input("Enter your name: ")
# text_message = returner(name)
# print(text_message)

# Advance :

# def magic(*args): # we can replace *args with *_______ whatever you want but it is a convention to use *args for variable length arguments
#     print("The magic number is:", sum(args))
#     return print(*args) # it does not allow to unpack tuple by a,b,c = args. 

# # tup = magic(1, 2, 3) # if we assign it then it gives none because it returns print(args) which is none but it prints the args as well as the sum of args
# print(tup)
# magic(1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3)

# *args concept

# def greet(name, *args, names_var):
#     print(f"Hello {name}!\n")
#     for names in args:
#         print(f"Hello {names}!")
#     return f"Hello {names_var}!"

# special_name = greet("Ali","Ibrahim","Ahmad Ali","Haroon","Hassan","Hussain", names_var="Sarim")
# print(special_name)


# **kwargs concept

# def myfun(**kwargs):
#     # print(kwargs) # it gives a dictionary of the keyword arguments
#     print(kwargs['fname'])
    
# names = {"fname":"Ali","lname":"Ahmad"}    
# # myfun(fname="Ali",lname="Ahmad")
# myfun(**names)

# def myfun(**kwargs):
#     for key ,value in kwargs.items():
#         print(f"key: {key} and value: {value}")
# names = {"fname":"Ali","lname":"Ahmad"}
# myfun(**names) 

# Local scope :

# def fun():

#     x = 1
#     def fun2():
#         print(x) # it is accessible because of closure and it is a nested function
#     fun2()

# fun()
# print(x)  # it is not run because x is a local variable and it is not accessible outside the function  

# Global scope Exercise :

# clothes = "dirty clothes"

# def washing_machine(clean_clothes):
#     clothes = clean_clothes
#     print(clothes)

# print(clothes)
# washing_machine("clean clothes")
# print(clothes) # it is not changed because we are not changing the global variable but we are creating a new local variable with the same name and assigning it a new value.`


clothes = "dirty clothes"

def washing_machine(clean_clothes):
    global clothes # we cann't assign a value to the global variable at the time of declaration. we can also use it inside another file.
    clothes = clean_clothes
    print(clothes)

print(clothes)
washing_machine("clean clothes")
print(clothes) # it is changed because we are using global keyword to change the global variable clothes and assign it a new value clean_clothes.



