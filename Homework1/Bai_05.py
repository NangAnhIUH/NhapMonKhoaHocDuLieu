def isPrime(n: int):
    if n < 2: # less than 2
        return False
    if n < 4: # 2 3
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

from math import sqrt, pow
n = int(input("Tim so nguyen to thu n: "))
# Su dung cong thuc tong quat:
can5 = sqrt(5)
fib = lambda n: int((pow((1 + can5) / 2, n) - pow((1 - can5) / 2, n)) / can5)
print(f"Fibonacci_{n} = {fib(n)}")