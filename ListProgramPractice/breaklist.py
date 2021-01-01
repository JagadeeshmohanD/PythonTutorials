# How many elements each list should have
my_list = [1,2,3,4,5,6,7,8,9]
n=4
#using list compreshension
final = [my_list[i*n:(i+1)*n] for i in range((len(my_list)+ n - 1)//n)]
print(final)

##########################################
# using list comprehension
l = [1,2,3,4,5,6,7,8,9]
n = 4
x = [l[i:i+n] for i in range(0,len(l),n)]
print(x)