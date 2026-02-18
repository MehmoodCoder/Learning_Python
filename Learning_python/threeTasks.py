# Task 1: Age Calculator
# Roman Urdu: Is task mein humein user se uski paidaish ka saal (Birth Year) as an input lena hoga. Phir maujooda saal (2026) mein se us birth year ko minus kar denge.

# Formula: 2026 - Birth Year

# English: In this task, we will take the user's birth year as an input. Then, we will subtract the birth year from the current year (2026).

# Formula: 2026 - Birth Year

birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print("Your age in 2026 will be:", age)


# Task 2: Pass/Fail Checker
# Roman Urdu: Ismein hum "if-else" condition lagayenge. Agar marks 40 ya us se zyada hain, to result "Pass" dikhayenge, warna "Fail".

# Logic: if marks >= 40 (Pass), else (Fail).

# English: In this, we will apply an "if-else" condition. If the marks are 40 or more, we will show the result as "Pass," otherwise "Fail."

# Logic: if marks >= 40 (Pass), else (Fail).


marks = int(input("Enter your marks out of 100: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")   


# Task 3: List Indexing
# Roman Urdu: Python mein counting 0 se shuru hoti hai. Isliye "Saib" ke liye 0 index aur "Angoor" ke liye 3 index use hoga.

# Indices: Saib = 0, Angoor = 3.

# English: In Python, counting starts from 0. Therefore, index 0 will be used for "Saib" and index 3 will be used for "Angoor."

# Indices: Saib = 0, Angoor = 3.

fruits = ["Saib", "Kela", "Amrood", "Angoor"]
print("Index of Saib:", fruits.index("Saib"))  # Output: 0
print("Index of Angoor:", fruits.index("Angoor"))  # Output: 3