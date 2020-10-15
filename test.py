class Dog:
    #Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"

class GoldenRetriver(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

class JackRusellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    def speak(self, sound="Woff")
    return super().speak(sound)

class Bulldog(Dog):
    def speak(self, sound="Woof")
    return super().speak(sound)

buddy = Dachshund("Buddy", 9)
miles = JackRusellTerrier("Miles", 4)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)