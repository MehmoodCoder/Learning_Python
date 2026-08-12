# nonlocal keyword :

phone = "iphone 16 on road" 

def parent_home():
    phone = "iphone 16 on parent home" # if you comment this line it causes error and forget it's behaviour
    def myhome():
        nonlocal phone
        # phone = "iphone 16 on my home"
        return phone 
    return myhome()


print(parent_home())
print(phone)


# global keyword :

phone = "iphone 16 on road" # if you comment this line it causes error.

def parent_home():
    phone = "iphone 16 on parent home" # it never searches in nonlocal
    def myhome():
        global phone
        # phone = "iphone 16 on my home"
        return phone 
    return myhome()


print(parent_home())
print(phone)


    
    

