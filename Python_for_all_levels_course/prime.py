# Prime Finder

no = int(input("Enter a number : "))
if no == 1:
    print(f"{no} is not prime")
else:    
    i ,flag = 2 ,1

    while i < no:
        if no%i == 0:
            flag = 0
        i=i+1
    if flag == 0:
        print(f"{no} is not prime")
    else:
        print(f"{no} is prime")