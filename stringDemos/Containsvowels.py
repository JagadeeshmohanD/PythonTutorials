# Python program to accept the strings which contains all the vowels
# Function for check if string is accepted or not
def checkvowels(str1):
    str1=str1.lower()
    vowels = set("aeiou")
    s = set({})
    for char in str1:
        if char in vowels :
            s.add(char)
        else:
            pass

    if len(s) == len(vowels):
        print("Vowels Accepted")
    else:
        print("Vowels not Accepted")

#drive code
if __name__ == "__main__":
    str1 = input("Enter string for vowels acceptance")
    print("The entered string for vowel is:"+str(str1))
    checkvowels(str1)

######################################################
#implementation 2.0
def checkvowels1(str1):
    if len(set(str1).intersection("AEIOUaeiou"))>=5:
        return ("Vowels Accepted1")
    else:
        return ("Vowels Not Accepted1")

#driving code
if __name__ == "__main__":
    print("The entered string for vowel1 is:"+str(str1))
    print(checkvowels1(str1))