import Bai_05

# Bai 05: Su dung isPrime nhu thu vien math.sqrt de lam lai bai 04
n = int(input("Nhap so n: "))
cnt = 0
print(f"10 SNT lon hon {n} la:")
while cnt < 10:
    if Bai_05.isPrime(n):
        print(n, end=" ")
        cnt += 1
    n += 1