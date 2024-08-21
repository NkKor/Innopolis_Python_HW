from abc import ABC,abstractmethod


class Animal(ABC):
    def __init__(self,age, weight, areal):
        self.areal = areal
        self.age = age
        self.weight = weight

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, age, weight, areal):
        super().__init__(age, weight, areal)

    def speak(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, age, weight, areal):
        super().__init__(age, weight, areal)

    def speak(self):
        print("Meow!")


class Dolphin(Animal):
    def __init__(self, age, weight, areal):
        super().__init__(age, weight, areal)

    def speak(self):
        print("Flipp!")


class Elephant(Animal):
    def __init__(self, age, weight, areal):
        super().__init__(age, weight, areal)

    def speak(self):
        print("Tooooo!")


class Orkestra:
    def __init__(self, animals: list[Animal]):
        self.animals = animals

    def sing(self):
        for animal in self.animals:
            animal.speak()


cat = Cat(5, 1, "Home")
dog = Dog(12, 13, "Garden")
dolphin = Dolphin(10, 40, "Sea")
elephant = Elephant(30, 1000, "Savanna")

ork = Orkestra([cat, dog, dolphin, elephant])
ork.sing()



