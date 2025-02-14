class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_info(self):
        return f"name: {self._name}, age: {self._age}"

person1 = Person("Daviti", 25)
person2 = Person("Giorgi", 30)
person3 = Person("Mariami", 35)

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
