x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
stepX = (x1-x2)
stepY = (y1 - y2)
if abs(stepX) == abs(stepY):
    print('YES')
else:
    print('NO')
