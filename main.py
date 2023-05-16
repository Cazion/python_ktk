def tpl_sort(data: tuple):
    lst = list(data)
    for el in lst:
        if type(el) == str:
            return data
    return tuple(sorted(data))


def slicer(data: tuple, element) -> tuple:
    if element not in data:
        return tuple()
    listed = list(data)

    start_index = listed.index(element)
    res = [listed[start_index]]
    start_index += 1

    while start_index < len(listed):
        res.append(listed[start_index])
        if listed[start_index] == element:
            break
        start_index += 1
    return tuple(res)


def sieve(data: list):
    return tuple(set(reversed(data)))


def deleting_el(data: tuple, element):
    if element not in data:
        return data
    result = list(data)
    result.remove(element)
    return tuple(result)


tpl = (23, 69, 13, 17, 18, 16, 97, 16, 15, 14, 13, 96, 1234, 1, 3, 1, 89)
print(tpl_sort(tpl))

print("\n\nTask 2 tests:")
print(slicer(tpl, 13))
print(slicer(tpl, 1))
print(slicer(tpl, 89))
print(slicer(tpl, 89678))

# Task 3 test
print("\n\nTask 3 test:")
print(sieve((list(tpl))))

# Task 4 tests
print("\n\nTask 4 tests:")
print(deleting_el(tpl, 43567))
print(deleting_el(tpl, 1))
print(deleting_el(tpl, 17))
