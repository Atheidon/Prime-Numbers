#A SIMPLE PRIME NUMBER GENERATOR

#importing required modules
import math
#The user gives a number x. This number doesn't count in the range.
rangE = int(input("Give a number which dictates the range: "))
def prime(number):
    #Filtering negative numbers, zero and one
    if number <= 1: return False
    #If the number is 2, print it.
    if number == 2:
        print(2)
        return True
    #Filtering even numbers
    if number % 2 == 0: return False

    #reducing more
    max_div = math.floor(math.sqrt(number))
    for i in range(3, 1 + max_div, 2):
        if number % i == 0:
            return False
    #If number is a prime number, print it.
    else:
        print(number)
        return True
#this is for counting the number of primes
amount = 0

for number in range(1,rangE):
    rangE = prime(number)
    amount += rangE
print("The total amount of prime numbers in the specified range:", amount)

input("press enter to exit")