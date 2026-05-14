def chees_and_buns(orogonal_fun):
    
    def wrap():
        print("I'm upper bread")
        orogonal_fun()
        print("I'm lower bread")
    return  wrap()       
# @chees_and_buns
def chicken():
    print("I'm roasted chicken")

# burger = chees_and_buns(chicken)

