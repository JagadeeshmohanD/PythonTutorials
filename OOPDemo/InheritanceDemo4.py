class A:
    def sum(self):
        print("calling from A-Sum of 2 number is 15")

class B(A):
    def sum(self):
        print("calling from B-sum of 2 number is 25")

class C(B):
    def sum(self):
        print("calling from C-sum of 2 number is 50")


obj1=C()
obj1.sum()

# obj2=B()
# obj2.sum()
#
# obj3=C()
# obj3.sum()

