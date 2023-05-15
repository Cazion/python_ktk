n = int(input())
last_num = 0
for i in range(1, n+1):
    last_num += i
    print(last_num)
    last_num *= 10
