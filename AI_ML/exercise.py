# Exercise :

# "Count the number of uppercase and lowercase letters in the given string."

# Solution 1 :

s = "a qUick Brown Fox juMps Over the LaZy Dog."



def letter_type_finder(s):
    capital_letters_counter = 0
    small_letters_counter = 0
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i in capital_letters:
            capital_letters_counter+=1
        elif i in small_letters:
            small_letters_counter+=1
        else:
            continue
    return f"The string contains {small_letters_counter} small letters and {capital_letters_counter} capital letters."        

print(letter_type_finder(s))
    
            
# Solution 2 :

string = "a qUick Brown Fox juMps Over the LaZy Dog."

def letter_type_finder1(s):
    counter = {"Upper_letters":0,"Lower_letters":0}
    
    for i in s:
        if i.isupper():
            counter["Upper_letters"]+=1
        elif i.islower():
            counter["Lower_letters"]+=1
        else:
            pass
    return f"""
    The string contains {counter["Lower_letters"]} lower letters.
    The string contains {counter["Upper_letters"]} upper letters."""
            
print(letter_type_finder1(string))




    

