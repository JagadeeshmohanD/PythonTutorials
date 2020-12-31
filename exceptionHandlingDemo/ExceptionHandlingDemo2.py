try:
    num1=int(input("please enter number 1"))
    num2=int(input("please enter number 2"))
    result=num1/num2
    print("Result is ",result)
except TypeError as err:
    print("please provide only digits",err)
except ZeroDivisionError as err:
    print("Please do not enter zero",err)
except ValueError as err:
    print("Please provide valid entry",err)
except Exception as err:
    print("something went wrong")

finally:
    print("Have a nice day")


