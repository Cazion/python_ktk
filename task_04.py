n = int(input())
hour = n % (60 * 24) // 60
minutes = n % 60
print(hour, minutes)
