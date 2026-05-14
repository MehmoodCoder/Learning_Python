print(dir())

for i in dir():
    # print(i)
    pass

for i in dir(__builtins__)   :
    # print(i)
    pass

for i in dir(__name__):
    print(i)

help(print)
    