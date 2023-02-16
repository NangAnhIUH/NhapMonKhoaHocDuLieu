# import Bai_05
from Bai_05 import isPrime

# Bai 05: Su dung isPrime nhu thu vien math.sqrt de lam lai bai 04
cnt = 0
n = int(input("Nhap so n: "))

print(f"10 SNT lon hon {n} la:")

while cnt < 10:
    if isPrime(n):
        print(n, end=" ")
        cnt += 1
    n += 1