import math
r = int(input("Give a number which dictates the range: "))
def prime(n):
    if n <= 1: return False
    if n == 2:
        print(2)
        return True
    if n % 2 == 0: return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: return False
    else:
        print(n)
        return True
a = 0
for n in range(1,r):
    r = prime(n)
    a += r
print("The total amount of prime numbers in the specified range:", a)
input("press enter to exit")