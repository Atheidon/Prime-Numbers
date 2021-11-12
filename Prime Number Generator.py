#Importing modules
import math
import time
#The user gives a number x. This number doesn't count in the range.
x = int(input("Give a number which dictates the range: "))
def is_prime(n):
    #Filtering negative numbers, zero and one
    if n <= 1:
        return False
    #If the n is 2, print it.
    elif n == 2:
        print(2)
        return True
    #Filtering even numbers
    elif n > 2 and n % 2 == 0:
        return False

    #reducing more
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    #If n is a prime number, print it.
    else:
        print(n)
        return True

#setting up a timer
# Driver function
t0 = time.time()
c = 0 #for counting
 
for n in range(1,x):
    x = is_prime(n)
    c += x
print("Total prime numbers in range :", c)

#printing the time
t1 = time.time()
print("Time required :", t1 - t0)

input("press enter to exit")
