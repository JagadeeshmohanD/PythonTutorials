#function to return all uncommon words
def uncommonwords(a,b):
    #count will contain all the word count
    count = {}
    #insert words of string a to hash
    for word in a.split():
        count[word] = count.get(word,0)+1
    #insert words of string b to hash
    for word in b.split():
        count[word] = count.get(word,0)+1
    #return required list of words
    return [word for word in count if count[word] == 1]

#driver code
a = input("Enter string a to validate common in b")
b = input("Enter string b to validate common in a")
#print required
print(uncommonwords(a,b))
