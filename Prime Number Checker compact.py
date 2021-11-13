n = int(input("Fill in a number you would like to check (to see if it's a prime number): "))
if n > 1:
    for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number, because",i,"*",n//i,"=",n,".")
           break
    else: print(n,"is a prime number")
else: print(n,"is not a prime number")
input("press enter to exit")