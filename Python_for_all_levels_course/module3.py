import module1
import module2
print(module1.a) # it is 6 because we have changed the value of a in module1 by importing it in module2 and changing its value to 6. and when we import module2 in this file, it also imports module1 and we can access the changed value of a in this file as well.
print(module1.y) # it is 100 because we have changed the value of y in module1 by importing it in module2 and changing its value to 100. and when we import module2 in this file, it also imports module1 and we can access the changed value of y in this file as well.