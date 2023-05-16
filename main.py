def calculator(n1, n2, oper):
    if oper == "+":
        return n1 + n2
    if oper == "-":
        return n1 - n2
    if oper == "*":
        return n1 * n2
    if oper == "/":
        if n2 == 0:
            print("Ошибка, деление на 0 невозможна")
            return 0
        return n1 / n2


def reverse(text):
    return ''.join(i for i in text[::-1])


names = list()
def robot_hello(name):
    global names
    if names.count(name) > 0:
        return f"Привет, {name}!"
    names.append(name)
    return f"Привет, {name}! Рад знакомству!"


def while_counter():
    i = 0
    while i <= 10:
        print(i, end=" ")
        i += 1


def rec_counter(num):
    print(num, end=" ")
    if num == 10:
        return num
    result = rec_counter(num + 1)
    return result


def while_fib():
    nums = [0, 1]
    while True:
        new_num = nums[-1] + nums[-2]
        if new_num > 100:
            break
        nums.append(new_num)
    return nums


def rec_fib(num, fib_nums):
    if len(fib_nums) < 2:
        return
    if num >= 100:
        return fib_nums
    num = fib_nums[-1] + fib_nums[-2]
    fib_nums.append(num)
    num = rec_fib(num, fib_nums)
    return fib_nums


result = calculator(27, 3, "-")
print(result)

result = reverse("Hello, World!")
print(result)

result = robot_hello("Vlad")
print(result)

result = robot_hello("Dima")
print(result)

result = robot_hello("Angelina")
print(result)

result = robot_hello("Vlad")
print(result)

result = robot_hello("Angelina")
print(result)

while_counter()

num = 0
rec_counter(num)

result = rec_fib([0, 1])