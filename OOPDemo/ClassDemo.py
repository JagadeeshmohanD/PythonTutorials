class person:

    def welcome(self):
        print("Hello Python")

    def hello_world(self):
        print("Hello World")

def outsideclass():
    print("Outside the class")

p=person()
p.welcome()
p.hello_world()

outsideclass()
