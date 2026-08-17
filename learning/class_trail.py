class Animal:
    def speak(self):
        print("animal", self)


class Dog(Animal):
    def speak(self):
        print("dog setup", self)
        super().speak()

dog = Dog()
dog.speak()