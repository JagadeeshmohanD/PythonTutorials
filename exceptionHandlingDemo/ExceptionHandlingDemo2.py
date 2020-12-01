try:
    content=open("C:\\Users\\Jagadeesh Mohan D\\PycharmProjects\\pythonTutorials\\Demo1.txt","r")
    print(content.read())
    print("Have a nice day")

except FileNotFoundError as err:
    print("Something went wrong",err)

print("This is last statement")
