#A SIMPLE PRIME NUMBER GENERATOR

#importing required modules
import math
#The user gives a number x. This number doesn't count in the range.
x = int(input("Give a number which dictates the range: "))
def prime(n):
    #Filtering negative numbers, zero and one
    if n <= 1: return False
    #If the n is 2, print it.
    if n == 2:
        print(2)
        return True
    #Filtering even numbers
    if n % 2 == 0: return False

    #reducing more
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    #If n is a prime number, print it.
    else:
        print(n)
        return True

c = 0

for n in range(1,x):
    x = prime(n)
    c += x
print("The total amount of prime numbers in the specified range:", c)

input("press enter to exit")