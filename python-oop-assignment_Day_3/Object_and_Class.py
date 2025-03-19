class Person:
    
    def __init__(self,name,age):
        self.name=name  # attributes
        self.age=age

person1=Person("Ram",22)  #creating object for Person class
print(person1.name)
print(person1.age)