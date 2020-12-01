class BaseClass:
    def hello_world(self):
        print("Hello Python from Base")
        
    def bye(self):
        print("Bye from python")

class ChildClass(BaseClass):
    def hello_world(self):
        super().hello_world()
        super().bye()
        # BaseClass.hello_world(self)
        print("Hello Python from child")

obj1=ChildClass()
obj1.hello_world()


