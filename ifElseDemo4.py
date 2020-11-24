status=False
names=["python","java","js","C#"]

for name in names:
    if name=="js":
        status=True
        break
    else:
        print("please wait we are still searching")

if status:
    print("we are glad that we found the record")
else:
    print("sorry we could not found the record")

