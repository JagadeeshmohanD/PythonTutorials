import os
# filepath=os.getcwd()
# fz=os.path.dirname(filepath)
# print(fz)
with open(os.path.dirname(os.getcwd())+"\\DemoNew.txt") as f:
    print("Current state is",f.closed)
    data=f.read()
    print(data)

print("Sate of the file is ",f.closed)