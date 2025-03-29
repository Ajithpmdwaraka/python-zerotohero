# Polymorphism: Different classes with the same method

class Bird:
    def sound(self):
        return "Chirp Chirp!"

class Duck(Bird):
    def sound(self):
        return "Quack Quack!"

class Crow(Bird):
    def sound(self):
        return "Caw Caw!"

animals = [Duck(), Crow()]

for animal in animals:
    print(animal.sound())
