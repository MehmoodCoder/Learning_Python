# Task: "The Vowel Counter" (Huroof-e-Illat ki counting)
# Aapko ek function banana hai jo ek sentence (string) lega aur us mein se sirf Vowels (a, e, i, o, u) ko gin kar batayega ke wo kitni baar aaye hain.

# Misal (Example):

# Input: "hello world"

# Vowels hain: e, o, o (Total: 3)

# Output hona chahiye: 3

# Sharaait (Rules):

# Aapko for loop istemal karna hai string ke har character par jane ke liye.

# Aapko ek Counter variable (shuru mein 0) rakhna hoga.

# Agar character vowel hai, to counter mein +1 kar dein.

# Hint: Yaad rakhein ke capital A aur small a dono vowels hain.

# program :

# def vowel(sentence):
#     count = 0
#     vowels = "aeiouAEIOU"
    
#     for char in sentence:
#         if char in vowels:
#             count += 1
            
#     return count

# sentence = input("Enter a sentence: ")

# print(vowel(sentence)) 

def vowel(sentence):
    count = 0
    countA = 0
    countE = 0
    countI = 0
    countO = 0
    countU = 0
    for char in sentence :
        if char in "aAEeiIOoUu" :
           count += 1
           if char in "aA" :
              countA += 1
           elif char in "eE" :
              countE += 1
           elif char in "iI" :
              countI += 1
           elif char in "oO" :
              countO += 1
           elif char in "uU" :
              countU += 1

    return count, countA, countE, countI, countO, countU

sentence = input("Enter a sentence: ")
total_vowels, countA, countE, countI, countO, countU = vowel(sentence)
print(f"Total Vowels: {total_vowels}")
print(f"Count of 'a' or 'A': {countA}")         
print(f"Count of 'e' or 'E': {countE}")
print(f"Count of 'i' or 'I': {countI}")
print(f"Count of 'o' or 'O': {countO}")
print(f"Count of 'u' or 'U': {countU}")









