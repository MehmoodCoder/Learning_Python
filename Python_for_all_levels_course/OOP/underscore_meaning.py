# Single Leading Underscoring: _var : Private Method or Attribute
class MyClass:
    def __init__(self):
        self._private_var = "This is a private variable"

    def _private_method(self):
        return "This is a private method"   
    
# Usage
obj = MyClass()
print(obj._private_var)  # Accessing the private variable (not recommended)
print(obj._private_method())  # Accessing the private method (not recommended)

# Single Trailing Underscore: var_ : Avoiding Conflicts with Python Keywords
class MyClass:
    def __init__(self, class_):
        self.class_ = class_  # Using a trailing underscore to avoid conflict with the 'class' keyword

# Usage
obj = MyClass("MyClass")
print(obj.class_)  # Accessing the variable (not recommended)

# Only underscore: _ : Throwaway, Unused Variable
for _ in range(5):
    print("This loop runs 5 times, but we don't care about the loop variable.")

# Double Leading Underscore: __var : Name Mangling for Class Attributes
class MyClass:
    def __init__(self):
        self.__private_var = "This is a private variable with name mangling"

    def __private_method(self):
        return "This is a private method with name mangling"    

# Usage
obj = MyClass()
# print(obj.__private_var)  # This will raise an AttributeError due to name mangling
# print(obj.__private_method())  # This will also raise an AttributeError due to name mangling

# Double Leading and Trailing Underscore: __var__ : Special Methods (Magic Methods)
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value: {self.value}"

# Usage
obj = MyClass(10)
print(obj)  # This will call the __str__ method and print "MyClass with value: 10"

print(dir(MyClass))  # This will show all the attributes and methods of MyClass, including special methods like __init__ and __str__)


