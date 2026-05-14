import sys

# Genrator :

def my_gen(no:int):
    start = 0
    while start < no:
        yield start
        start += 1

gen_list = my_gen(100)

print(f"This generator takes {sys.getsizeof(gen_list)} bytes.")

print("x"*30)

# By for loop

iter_list = []

for val in gen_list:
    iter_list.append(val)


print(f"This normal list takes {sys.getsizeof(iter_list)} bytes.")


