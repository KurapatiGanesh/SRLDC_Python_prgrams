class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"
    
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())