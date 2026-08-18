# ------------------------------------------------------------------
# PYTHON WALRUS OPERATOR (:=) EXPLAINED
# ------------------------------------------------------------------

# TRADITIONAL APPROACH (Old Way)
# Pehle list banate hain, length calculate karte hain, aur phir condition check karte hain:
numbers = [10, 20, 30, 40, 50]
n = len(numbers)
if n > 3:
    print(f"List is long! It has {n} elements.")


# WALRUS OPERATOR APPROACH (Modern & Clean Way)
# Assign 'n = len(numbers)' AND evaluate 'n > 3' at the EXACT SAME TIME inside the if-statement!
if (n := len(numbers)) > 3:
    print(f"List is long! It has {n} elements.")


# REAL-WORLD USE CASE: CLEANER LOOPS
# Purana tareeqa: User input lene ke liye 'while True' aur inside 'if/break' likhna padta tha.
# Naya tareeqa: User input aur condition check dono WHILE condition ke andar ek line mein:

print("\n--- Interactive Loop Example ---")
# Loop chalta rahega jab tak user 'quit' na likh de
while (user_input := input("Type something ('quit' to exit): ")) != "quit":
    print(f"You entered: {user_input.upper()}")


# RULE OF THUMB:
# Walrus operator (:=) code lines kam karta hai aur repetitive function calls (jaise len()) ko bachata hai.