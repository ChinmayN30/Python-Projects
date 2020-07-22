class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f"My name is {self.name}")


john = Person("John")
bob = Person("Bob")
john.talk()
bob.talk()


