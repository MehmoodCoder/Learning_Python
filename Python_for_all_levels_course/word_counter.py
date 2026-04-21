article = "Some people have curly brown hair through proper brushing. Some people have straight blonde hair through proper brushing. Some people have curly blonde hair through proper brushing. Some people have straight brown hair through proper brushing."
word_counter ,char_counter,char_counter_without_spaces = 1,0,0

for i in article:
    char_counter += 1
print(f"The given article have {char_counter} characters including white spaces.")  

for j in article:
    if j in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        char_counter_without_spaces += 1
print(f"The given article have {char_counter_without_spaces} characters including without white spaces.")  

for k in article:
    if k == " ":
        word_counter += 1
print(f"The given article have {word_counter} words.")   
