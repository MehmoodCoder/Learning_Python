with open("Python_for_all_levels_course/file.txt","a") as file:
    for i in range(1,10):
        for j in range(1,10):
            file.write(f"{i} x {j} = {i*j}\n")
