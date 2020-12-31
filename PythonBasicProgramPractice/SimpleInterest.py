def simple_interest(p,t,r):
    print('The Principle is',p)
    print('The time period in months',t)
    print('the Rate of interest is',r)
    si=(p*t*r)/100
    print('The Simple Interest is',si)
    return si
#driver code
p=float(input('The principle amount'))
t=float(input('The time period in months'))
r=float(input('The Rate of interest'))
simple_interest(p,t,r)
