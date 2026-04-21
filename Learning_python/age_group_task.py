age = [13,18,45,67,3,85,44,23,42,28,19,77,11,6,65,54]
groups = {"group 0 to 18" : 0,"group 19 to 30" : 0,"group 31 to 60" : 0, "group 61 to 90" : 0}
for i in age:
    if i >= 0 and i <=90:
        if i <= 18:
            groups["group 0 to 18"]+=1
        elif i <= 30:
            groups["group 19 to 30"]+=1
        elif i <= 60:
            groups["group 31 to 60"]+=1
        elif i <= 90:
            groups["group 61 to 90"]+=1
    else:
        print("you are not in any age of group !")

print(f"{groups["group 0 to 18"]} ages occur in 0 to 18 age group") 
print(f"{groups["group 19 to 30"]} ages occur in 19 to 30 age group") 
print(f"{groups["group 31 to 60"]} ages occur in 31 to 60 age group") 
print(f"{groups["group 61 to 90"]} ages occur in 61 to 90 age group") 
