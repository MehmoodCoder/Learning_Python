class map():
    # Attribute
    mat = "Blue Mat"
    print(f"I make {mat}.")
    # Method
    def adder(self):
        return 4+4
    
        

caller = map()

print(caller.mat)
print(caller.adder())


mat = map()
mat.mat = "Red"
print(mat.mat)

mat.mat2 = "Black mat"
print(mat.mat2)

mat2 = map()
mat2.mat = "White"
print(mat2.mat)

mat3 = map()
mat3.mat = "Purple"
print(mat3.mat)


class map():
    def __init__(self,mat):
        print(f"I make {mat}.")

mat1 = map("Green Mat")
mat1 = map("Voilent Mat")
mat1 = map("Gold Mat")
mat1 = map("Simple Mat")



    
    