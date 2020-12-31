def compound_interest(principle,rate,time):

    #calculate compound interest
    # Amount: float =0
    # CI: float=0
    Amount = principle*(pow((1+rate/100),time))
    CI=float(Amount-principle)
    print("Compound Interest is",CI)

#driver code
principle=float(input('The principle amount'))
time=float(input('The time period in months'))
rate=float(input('The Rate of interest'))
compound_interest(principle,rate,time)
