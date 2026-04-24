import module1 
result = module1.sum(1,2)
print(f"Sum from Module1 = {result}")

module1.a = 6
module1.y = 100

# print(module1.a) # we can use global variable without assigning it at global scope in another module.
# print(module1.y) # we cann't use global variable without assigning it at global scope in another module.
