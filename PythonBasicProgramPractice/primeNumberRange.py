# Python program to print all
# prime number in an interval
#number should be greater than 1
start = int(input('Enter start range'))
end = int(input('Enter end range'))
for i in range (start,end):
    if i > 1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)

