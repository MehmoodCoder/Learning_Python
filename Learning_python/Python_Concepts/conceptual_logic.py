# ------------------------------------------------------------------
# PYTHON MEMORY IDENTITY: SCRIPT VS. INTERACTIVE REPL EXPLAINED
# ------------------------------------------------------------------

# 1. SMALL INTEGER CACHING (-5 to 256)
# Python pre-loads numbers -5 to 256 in memory at startup.
a = 256
b = 256
print(a is b)  # True: Both point to the pre-allocated cache in RAM.


# 2. COMPILER OPTIMIZATION (THE SURPRISE)
x = 257
y = 257
print(x is y)  
# Result: True (in .py script) | False (in terminal/REPL)
# Why? Running a .py file compiles the entire code block at once.
# Python detects identical constants (257) and reuses the memory block.
# In a terminal, lines run one-by-one, so 257 gets separate memory blocks.


# 3. STRING INTERNING
s1 = "hello!"
s2 = "hello!"
print(s1 is s2) 
# Result: True (in .py script) | False (in terminal/REPL)
# Same concept: Script compilation pools identical string constants together.


# 4. HOW TO PROVE IT (CHECK MEMORY ADDRESSES)
# Use id() to print the actual memory location of variables:
print("Memory address of x:", id(x))
print("Memory address of y:", id(y))
print("Are they identical?", id(x) == id(y))  # True in script file


# RULE OF THUMB:
# Use '==' for checking values (e.g., x == y).
# Use 'is' ONLY for checking identity/singletons (e.g., x is None).