import random

# Super Class

class Enemy:

    def __init__(self,name = "Enemy",hit_points = 0,lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = True
    def damage(self,damage):    
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f"I take bullet took {damage} points damage, my remaining life is {remaining_points}")
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"{self.name} lost lives.")
            else:
                print(f"{self.name} is dead.")
                self.lives = False

    def __str__(self):
            return f"Name: {self.name}, Hit Points: {self.hit_points}, Lives: {self.lives}"

# inheritance
# Sub Classes

class Bone_scacher(Enemy):

    # Method Overloading

    def __init__(self,name = "Bone Scacher"):
        super().__init__(name = name, hit_points = 20, lives = 1)

    # def __init__(self, name="Bone Scacher", hit_points=20, lives=1):
    #     self.name = name
    #     self.hit_points = hit_points
    #     self.lives = lives

    # Error :

    # def __init__(self,name):
    #   pass   
    
    # because python gives priority to the method in the sub class,
    # so it will not call the method in the super class.

    def Snacher(self):
        return (f"{self.name} is snaching bones.")

class Blood_drinker(Enemy):
    def __init__(self,name = "Blood Drinker"):
        super().__init__(name = name, hit_points = 40, lives = 3)

    def skipped(self):
        if random.randint(1,5)==5:
            print(f"*** {self.name} ducked and saved")
            return True
        else:
            return False

    def damage(self,damage):
        if not self.skipped():
            super().damage(damage=damage)


class KingBloodDrinker(Blood_drinker):

    def __init__(self,name = "King Blood Drinker"):
        super().__init__(name)
        self.hit_points = 120

    def damage(self, damage):
        super().damage(damage//4)

class Brain_Eater(Enemy):
    pass




