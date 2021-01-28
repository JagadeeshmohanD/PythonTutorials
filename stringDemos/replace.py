def replace(test_str):
    test_list = test_str.split(' ')
    res = set()
    for idx, ele in enumerate(test_list):
        if ele in repl_dict:
            if ele in res:
                test_list[idx] = repl_dict[ele]
            else:
                res.add(ele)
    res = '  '.join(test_list)
    return res

#drive
test_str = input("Enter the string for replace")
print("The original string is :"+ str(test_str))
repl_dict = input(tuple)
print("Given tupple:"+ str(repl_dict))
#print result
print("The string after replacing :"+replace(test_str))