file = open("Python_for_all_levels_course/file.txt", "r")

print(file.read())

# for line in file:
#     print(line,end="")

# print(*file)

# print(file)

# print(file.readline())

file.close()

print("x"*30)

with open("Python_for_all_levels_course/file.txt", "r") as file:
    print(file.read())
    print("x"*30)



with open("Python_for_all_levels_course/file.txt", "r") as file:
    line_lists = file.readlines()
    # print(line_lists)
    for line in line_lists[::-1]:
        print(line,end="")
        # print(line.strip())
print("x"*30)

# Exercise :

with open("Python_for_all_levels_course/file.txt", "r") as file:
    chararcters = file.read()
    print(chararcters)
    print("x"*30)
    for char in chararcters[::-1]:
        print(char,end="")
