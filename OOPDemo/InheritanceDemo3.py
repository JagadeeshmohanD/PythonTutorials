class classA:
    def methodA(self):
        print("I am comming from Class A")
    def hello_world(self):
        print("hello from class A")

class classB:
    def methodB(self):
        print("I am Comming from Class B")
    def hello_world1(self):
        print("hello from class B")


class classC(classA,classB):
    def methodC(self):
        print("I am Comming from Class C")
    def hello_world2(self):
        print("hello from class C")

c=classC()
c.methodA()
c.methodB()
c.methodC()
c.hello_world1()
c.hello_world2()
print(classC.mro())
