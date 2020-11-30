# emp={"QA":'Jags',"Dev":'Kushi',"DevOps":'future',"Security":90,50:"Pyhton"}
# print(emp)
# print(type(emp))
# print(emp["QA"])
# print(emp.get("Dev"))

emp={"QA":['Jags','Rahul','David'],"Dev":'Kushi',"DevOps":'future',"Security":90,50:"Pyhton"}
#print(emp["QA"][1])
emp1=emp["QA"]
#print(emp1)

emp={"QA":"Jags","Dev":{"frontend":"Neha","backend":"Rush"}}
#print(emp["Dev"]["frontend"])

emp1=emp.get("Dev")
emp_name=emp1.get("backend")
print(emp_name)
print(emp["Dev"]["backend"])

emp["manager"]="XYZ"
print(emp)

emp["manager"]="joe Bidan"
print(emp)

# emp.pop("QA")
# print(emp)
print("*********************************")
print(emp)
emp.popitem()
print(emp)

