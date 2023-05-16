def countdown():
    yield from [x for x in range(10, -1, -1)]


def eng_alphabet():
    yield from [chr(ch) for ch in range(ord('a'), ord('z')+1)]


def fib(limit):
    last_num, new_num = 0, 1
    for _ in range(limit):
        yield last_num
        last_num, new_num = new_num, last_num + new_num


def fib_iteration(limit=10):
    data = fib(limit=limit)
    print("Method 1:", end=" ")
    for el in data:
        print(el, end=" ")
    print("\nMethod 2:", end=" ")

    data = fib(limit)
    while True:
        print(next(data), end=" ")


def even_nums(limit=21):
    yield from [num for num in range(limit) if num % 2 == 0]


def task6(start=1, limit=24):
    return {key: chr(value) for key, value in zip(range(start, limit), range(ord('a'), ord('a') + limit))}
