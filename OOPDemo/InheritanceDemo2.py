class classA:
    def methodA(self):
        print("I am comming from Class A")
    def hello_world(self):
        print("hello from class A")

class classB(classA):
    def methodB(self):
        print("I am Comming from Class B")
    def hello_world(self):
        print("hello from class B")


class classC(classB):
    def methodC(self):
        print("I am Comming from Class C")
    def hello_world(self):
        print("hello from class C")

obj1=classC()
obj1.methodA()
obj1.methodB()
obj1.methodC()
obj1.hello_world()
