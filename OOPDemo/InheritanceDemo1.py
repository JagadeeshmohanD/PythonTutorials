class Base:
    name="Jags"
    def baseMethod(self):
        print("I am in Base Class")

class Child(Base):
    company="Apple"
    def chilMethod(self):
        print("I am in child class")

c=Child()
c.chilMethod()
c.baseMethod()
print(c.name)
print(c.company)
