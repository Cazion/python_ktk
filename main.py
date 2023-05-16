from abc import abstractmethod
from time import time, localtime


class Animal:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.color = ""

    @abstractmethod
    def say():
        pass


class Cat(Animal):
    @staticmethod
    def say():
        return "Meow!"


class Dog(Animal):
    @staticmethod
    def say():
        return "Woof!"


class Father:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname


class Child(Father):
    def __init__(self, name, surname, patronim) -> None:
        super().__init__(name, surname)
        self.patronim = patronim

    def __str__(self) -> str:
        return f"{self.name} {self.surname} {self.patronim}"


class Stationary:
    def __init__(self, title="Канцелярия"):
        self.title = title

    @staticmethod
    @abstractmethod
    def draw():
        pass

    def set_color(self, value):
        self.color = value


class Pen(Stationary):
    color: str

    def __init__(self, title="Ручка", color="blue"):
        super().__init__(title)
        self.color = color

    @staticmethod
    def draw():
        return "Ручка пишет"


class Pencil(Stationary):
    def __init__(self, title="Карандаш"):
        super().__init__(title)

    @staticmethod
    def draw():
        return "Карандаш пишет"


class Handle(Stationary):
    def __init__(self, title="Маркер"):
        super().__init__(title)

    @staticmethod
    def draw():
        return "Маркер пишет"


class User:
    def __init__(self, login, password):
        self.login=login
        self.password=password

    def view(self):
        return f"Я - User. Могу просматривать содержимое"
    

class Moderator(User):
    def __init__(self, login, password, group_id):
        super().__init__(login, password)
        self.group_id = group_id

    def view(self):
        return "Я - Moderator. Могу просматривать содержимое"
    
    def redact(self):
        return "Я - Moderator. Могу редактировать содержимое"
    

class Clock:
    @staticmethod
    def say_time():
        cur_time = localtime(time())
        return f'{cur_time.tm_hour}:{cur_time.tm_min}:{cur_time.tm_sec}'


def task1():
    cat = Cat()
    dog = Dog()
    print(cat.say())
    print(dog.say())


def task2():
    child = Child("Aleks", "Alekseev", "Rodionovich")
    print(child)


def task3():
    pen = Pen()
    pencil = Pencil()
    handle = Handle()
    print(pen.draw())
    print(pencil.draw())
    print(handle.draw())

    pen.set_color("yellow")
    pencil.set_color("yellow")
    handle.set_color("yellow")
    print(pen.color)
    print(pencil.color)
    print(handle.color)


def task4():
    user = User("qwerty", "uiop")
    moder = Moderator("qwerty", "uiop", 54353)
    print(user.view())
    print(moder.view())
    print(moder.redact())


def task5():
    clock = Clock()
    print(clock.say_time())


task1()
task2()
task3()
task4()
task5()