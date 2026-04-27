def fabanucci(n):
    if n > 2:
        return fabanucci(n-1) + fabanucci(n-2)
    else:
        return 1

for i in range(1,101):# it does not run fastly so it is not relible.
    print(f"{i}th fabanucci number is {fabanucci(i)}")
