a = int(input())
b = int(input())
c = int(input())
if a == b and a == c:
    print(3)
elif a == b and a != c or b == c and a != b or a == c and b != c:
    print(2)
else:
    print(0)
