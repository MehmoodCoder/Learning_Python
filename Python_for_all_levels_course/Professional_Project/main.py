from player import player
from enemy import Enemy, Bone_scacher, Blood_drinker, Brain_Eater, KingBloodDrinker


# Mehmood = player("Mehmood")
# print(Mehmood.name)
# print(Mehmood)
# Mehmood.lives = 20
# print(Mehmood.lives)
# print(Mehmood)
# Mehmood.level = 5
# Mehmood.level += 2
# print(Mehmood.level)
# print(Mehmood.score)
# print(Mehmood)

# enemy1 = Enemy("Enemy1", 100,1)
# print(enemy1)
# enemy1.damage(30)
# print(enemy1)
# enemy1.damage(80)
# print(enemy1)
# enemy1.damage(50)
# print(enemy1)
# enemy1.damage(30)
# print(enemy1)
# enemy1.damage(80)
# print(enemy1)
# enemy1.damage(50)
# print(enemy1)

# Enemy1 = Bone_scacher("Bone Scacher")
# print(Enemy1)
# Enemy1.damage(20)
# print(Enemy1)
# print(Enemy1.Snacher())

# while Enemy1.lives:
#     Enemy1.damage(2)
#     print(Enemy1)

# vampire = Blood_drinker("Blood Drinker")

# while vampire.lives:
#     vampire.damage(4)
#     print(vampire)

king = KingBloodDrinker("King Blood Drinker")
print(king)

while king.lives:
    king.damage(20)
    print(king)


