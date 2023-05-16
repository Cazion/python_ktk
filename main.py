class Batary:
    def __init__(self, capacity, max_charge=5):
        self.capacity = capacity
        self.max_charge = max_charge

    def charge(self):
        if len(self.capacity) >= self.max_charge:
            return
        self.capacity.append(')')

    def discharge(self):
        if len(self.capacity) <= 0:
            return
        self.capacity.pop()

    def __str__(self):
        return f"[{''.join(self.capacity)}]"


class Queue:
    def __init__(self, *names):
        self.inside = list(names)

    def add(self, value):
        self.inside.append(value)

    def take_out(self):
        if len(self.inside) <= 0:
            return

        curr = 1
        while curr != len(self.inside):
            self.inside[curr-1] = self.inside[curr]
            curr += 1
        self.inside.pop()

    def __add__(self, value):
        self.add(value)

    def __iadd__(self, value):
        self.add(value)

    def __sub__(self, value):
        self.take_out()

    def __isub__(self, value):
        self.take_out()

    def __str__(self) -> str:
        return '=>'.join(self.inside)


class Matrix:
    def __init__(self, arrays: list[list]):
        self.matr = arrays

    def __add__(self, value):
        if not isinstance(value, Matrix):
            raise TypeError("You gave me not a matrix")
        if not (self.__is_rectangular and value.__is_rectangular):
            raise ArithmeticError("Matrices aren't equal to each other")

        matr = []
        for i in range(len(self.matr)):
            row = []
            for j in range(len(self.matr[i])):
                sum = self.matr[i][j] + value.matr[i][j]
                row.append(sum)
            matr.append(row)
        return Matrix(matr)

    def __str__(self):
        view = ''
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                view += f"{self.matr[i][j]:<5}"
            view += '\n'
        return view


def task1():
    batary = Batary([')', ')', ')', ')'], max_charge=15)
    print(batary)
    batary.charge()
    batary.charge()
    batary.discharge()
    batary.discharge()
    batary.charge()
    print(batary)
    batary.discharge()
    print(batary)
    batary.discharge()
    print(batary)


def task2():
    q = Queue("Sasha", "Petrov")
    q - None
    q + "Danil"
    q.add("Evgeny")
    q.add("Vasya")
    q.add("Gerorgie")
    q.add("Picasso")
    q.add("Pushkin")
    q.add("Putin")

    print(q)
    for i in range(len(q.inside) - 2):
        q.take_out()
    q.take_out()
    q.take_out()
    print(q)


def task3():
    matr1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matr2 = Matrix([[6, 5, 4], [3, 2, 1]])
    matr3 = matr1 + matr2
    print(matr3)


task1()
task2()
task3()
