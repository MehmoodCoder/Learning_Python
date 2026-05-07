import os
list1 = os.walk("Python_for_all_levels_course") # it is used to get the list of all files and directories in a directory and its subdirectories.



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


# 2.
def li_dir(s):
    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d,f)
            if os.path.isdir(current_dir):
                print("\t"*tab_stop + " Directory "+ f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print(f)
                
    tab_stop=0
    
    if os.path.exists(s):
        print("Directory Listing of " + s)
        dir_list(s)
        
    else:
        print(s+ " Directory does not exist!")


li_dir("Python_for_all_levels_course")
        


        

