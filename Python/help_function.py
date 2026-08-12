help(print)

def adder(a,b):
    
    # doc string is different from # comment.
    
    """
    This function takes two numbers as input and returns their sum.
    """
    return a+b

# i need to describe adder() as we saw print() use in help() so i use doc string

help(adder)

# Alternative help()

print(adder.__doc__)

# help(help)



