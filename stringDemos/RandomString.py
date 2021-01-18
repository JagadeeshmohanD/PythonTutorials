# Python program to generate and match  the string from all random strings of same length
import string
import random
import time

# all possible characters including  lowercase, uppercase and special symbols
# def random(t):
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'
t = "geek"
attemptThis = ' '.join(random.choice(possibleCharacters) for i in range(len(t)))
attemptNext = ''
completed = False
iteration = 0

while completed == False:
    print(attemptThis)

    attemptNext = ''
    completed = True

    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += t[i]

    iteration += 1
    attemptThis = attemptNext
    time.sleep(0.1)


#drive code
print("Target matched after "+str(iteration)+"iterations")