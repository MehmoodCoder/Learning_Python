# ------------------------------------------------------------------
# PYTHON WALRUS OPERATOR (:=) EXPLAINED
# ------------------------------------------------------------------

# TRADITIONAL APPROACH (Old Way)
# First create a list, calculate its length, and then check the condition:
numbers = [10, 20, 30, 40, 50]
n = len(numbers)
if n > 3:
    print(f"List is long! It has {n} elements.")


# WALRUS OPERATOR APPROACH (Modern & Clean Way)
# Assign 'n = len(numbers)' AND evaluate 'n > 3' at the EXACT SAME TIME inside the if-statement!
if (n := len(numbers)) > 3:
    print(f"List is long! It has {n} elements.")


# REAL-WORLD USE CASE: CLEANER LOOPS
# Traditional way: Required a 'while True' loop with an internal 'if/break' statement to get user input.
# Modern way: Combine user input and condition check directly inside the WHILE condition in a single line:

print("\n--- Interactive Loop Example ---")
# The loop keeps running until the user enters 'quit'
while (user_input := input("Type something ('quit' to exit): ")) != "quit":
    print(f"You entered: {user_input.upper()}")


# RULE OF THUMB:
# The walrus operator (:=) reduces boilerplate lines and prevents redundant/repetitive function calls (e.g., len()).