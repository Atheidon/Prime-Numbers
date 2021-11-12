import math
import time
x = int(input("Give a number: "))
def is_prime(n):
    if n <= 1: return False
    if n == 2:
        print(2)
        return True
    if n > 2 and n % 2 == 0: return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0: return False
    else: 
        print(n)
        return True
t0 = time.time()
c = 0
for n in range(1,x):
    x = is_prime(n)
    c += x
print("Total prime numbers in range :", c)
t1 = time.time()
print("Time required :", t1 - t0)
input("press enter to exit")