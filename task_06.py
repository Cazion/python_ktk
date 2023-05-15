from math import pow
nums = int(input())
result = 0
for i in range(1, nums+1):
    result += int(pow(i, 3))
print(result)
