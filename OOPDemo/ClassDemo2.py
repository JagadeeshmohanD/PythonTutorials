class person:

    def welcome(self):
        print("Hello Python")

    def hello_world(self):
        print("Hello World")

    def sum(self,num1,num2):
        print(num1+num2)

p=person()
p.name="jags"
p.phone=90909090
p.country="India"
p.city="Bengaluru"

q=person()
q.name="carz"
q.phone=80808080
q.country="USA"
q.city="Atlanta"

print(p.name)
print(q.country)
print(p.city)
