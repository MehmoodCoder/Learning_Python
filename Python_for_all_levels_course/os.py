import os
list1 = os.walk("C:\\Users\\Mehmood\\Desktop\\Python for all levels course") # it is used to get the list of all files and directories in a directory and its subdirectories.



for root, dirs, files in list1:
    print(f"Root: {root}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")
    print("\n")

for root, dirs, files in list1:
    print(root)
    for i in dirs:
        print(i)
    for file in files:
        print(file) 

