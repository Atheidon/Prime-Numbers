#A SIMPLE PRIME NUMBER CHECKER

#asking for a number to check
number = int(input("Fill in a number you would like to check (to see if it's a prime number): "))

#Primes can only be positive and one isn't a prime, so it filters those out.
if number > 1:
    #checking for factors of the given number:
    #Taking i in the range 2 - given number.
    for i in range(2,number):
        #If the number is is divisible by i, it's not a prime number,
       if (number % i) == 0:
           #and thus it prints that it isn't a prime number (it also prints the first factors it comes across), and stops.
           print(number,"is not a prime number, because",i,"*",number//i,"=",number,".")
           break
    #If the programm doesn't find any factors, the number must only be divisible by 1 and itself, and it must be a prime number.
    else:
       print(number,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(number,"is not a prime number")
input("press enter to exit")