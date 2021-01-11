#Method #1 : Using title() + replace()
def stp(test_str):
    res = test_str.replace("_"," ").title().replace(" ","")
    print("The string after changing case :" + str(res))

# #driving function
test_str = input("Enter the string for STP")
print("The given string :"+ test_str)
stp(test_str)

####################################################
#using capwords()
import string
res1 = string.capwords(test_str.replace("_"," ")).replace(" ","")
print("The string after changing case : "+str(res1))
