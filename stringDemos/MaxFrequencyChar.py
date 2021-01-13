# using naive method to get Least Frequent Character in String
def maxFreqChar(test_str):
    all_freq = {}
    for i in test_str:
        if i in all_freq:
            all_freq[i] +=1
        else:
            all_freq[i] = 1
    res = max(all_freq,key=all_freq.get)
    return res

#driving code
test_str = input("Enter the string to find leastFrequency")
print("The given string for LeastFrequencyChar :"+test_str)
print("The Minimum of all character in GeeksforGeeks is :" +str(maxFreqChar(test_str)))

###########################################################
from collections import Counter
def maxFreqChar1(test_str):
    res1 =Counter(test_str)
    res1 =max(res1,key=res1.get)
    return res1

print("The original string is :"+test_str)
print("The minimum of all character is :"+str(maxFreqChar1(test_str)))