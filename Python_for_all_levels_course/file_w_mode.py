fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango', 'strawberry', 'blueberry', 'watermelon', 'peach', 'pear']
with open("Python_for_all_levels_course/fruits.txt", "w") as fruit_file:
    for i, fruit in enumerate(fruits):
        fruit_file.write(f"{i+1}. {fruit}\n")
    fruit_file.write("\n")    
    for fruit in fruits:
        print( fruit,file=fruit_file)
