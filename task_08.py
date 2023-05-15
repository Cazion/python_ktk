n = int(input())
fac_mul = 1
fac_sum = 0
for i in range(1, n+1):
    fac_mul *= i
    fac_sum += fac_mul
print(fac_sum)
