# Local scope rules :

phone = "Iphone on road" # if you comment it then it causes error

def my_home():
    # phone = "Iphone on home" # comment this to see result
    return phone

# print(my_home())
# print(phone) 
# comment these print() to work more


# output :
#     Iphone on road
#     Iphone on road

# 2.

# Local Scope finds phone rule marked 

phone = "iphone 16 on road" #...3

def parent_home():
    # phone = "iphone 16 on parent home" #..2
    def myhome():
        # phone = "iphone 16 on my home" # ..1
        return phone 
        # return max # buildin function ... 4
    return myhome()


print(parent_home())
print(phone)











    
    
    
    
    
    


















