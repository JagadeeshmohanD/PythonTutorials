def replace_str(test_str):
    res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])
    return res

#driving code
test_str = input("Enter the string for validation")
print("The original string is :"+str(test_str))
word_list = input(tuple)
print("The original Tuple is :"+str(word_list))
repl_wrd = input("Enter the string for replace")
print("The original replace word is :"+str(repl_wrd))
print("string after multiple replace :"+replace_str(test_str))
############################################################
import re
def replace_str1(test_str):
    res1 = re.sub("|".join(sorted(word_list, key = len, reverse = True)), repl_wrd, test_str)
    return res1
#driving code2
print("string after multiple replace1 :"+replace_str1(test_str))