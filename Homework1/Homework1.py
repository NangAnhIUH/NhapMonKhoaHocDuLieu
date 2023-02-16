from math import sqrt, pow

# Bai 02: Chuyen so nguyen to thanh ham isPrime(n)
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

# Bai 03: Dung ham tren de in ra cac so nguyen to trong khoang [a, b]
# voi a, b nhap tu ban phim
a, b = map(int, input("Nhap [a, b] = ").split())
for i in range(a, b + 1):
    if isPrime(i):
        print(i, end=" ")

# Bai 04: Dung ham tren de in ra 10 so nguyen to lon hon n
# voi n nhap tu ban phim
cnt = 0
n = int(input("\nNhap so n: "))

print(f"10 SNT lon hon {n} la:")

while cnt < 10:
    if isPrime(n):
        print(n, end=" ")
        cnt += 1
    n += 1

# Bai 05: Bai_05.py va Bai_05_import.py

# Bai 06: Tim so Fibonacci thu n su dung lambda function
n = int(input("Tim so nguyen to thu n: "))

# Su dung cong thuc so hang tong quat:
can5 = sqrt(5)
fib = lambda n: int((pow((1 + can5) / 2, n) - pow((1 - can5) / 2, n)) / can5)
print(f"Fibonacci_{n} = {fib(n)}")