# Polymorphism

# Ploy = many 
# morphism = forms,shapes

class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Bird:
    def speak(self):
        return "Tweet!"


# Polymorphic function

def make_animal_speak(animal):
    print(animal.speak())


# Usage

dog = Dog()
cat = Cat()
bird = Bird()

make_animal_speak(dog)   # Output: Woof!
make_animal_speak(cat)   # Output: Meow!
make_animal_speak(bird)  # Output: Tweet!

# Polymorphic behavior with a list of animals

animals = [Dog(), Cat(), Bird()]

for animal in animals:
    make_animal_speak(animal)

# Output:

# Woof!
# Meow!
# Tweet!