from time import sleep


class Cat():

    def meow(self):
        return "Meow"

    def purring(self):
        return "Pure"

    def sleep(self):
        return "I'm sleeping"


class Good():
    def __init__(self, name, price, weight) -> None:
        self.name = name
        self.price = price
        self.weight = weight
        self.calc()

    def calc(self) -> None:
        self.cost = self.price * self.weight

    def __str__(self) -> str:
        return f"{self.name} costs {self.cost} for {self.weight} KG"


class Car():
    color:          str
    brand:          str
    body:           str
    speed:          float
    transmission:   str
    restrictions:   dict = {
        "truck": 60.0,
        "sedan": 80.0
    }

    def __init__(self, color: str, brand: str, body: str, speed: float, transmission: str) -> None:
        self.color = color.lower()
        self.brand = brand.lower()
        self.body = body.lower()
        self.transmission = transmission
        if not self.__check_speed(speed):
            self.speed = speed
        else:
            self.speed = self.restrictions[self.body]

    def start(self) -> str:
        return "Это мой последний заезд..."

    def stop(self) -> str:
        return "Это был мой последний заезд..."

    def turn(self, side: str) -> str:
        return f"Car is turned to the {side}"

    def speed_up(self, value: float) -> str:
        new_speed = self.speed + value
        if self.__check_speed(new_speed):
            return f"Speed hasn't been changed"

        old_speed = self.speed
        self.speed += value
        return f"Speed has been changed: {old_speed} -> {self.speed}"

    def speed_down(self, value: float) -> str:
        old_speed = self.speed
        self.speed -= value
        return f"Speed has been changed: {old_speed} -> {self.speed}"

    def beep(self) -> str:
        return "Союз нерушимый республик свободных....."

    def __check_speed(self, value: float):
        restr_speed = self.restrictions[self.body]
        if restr_speed < value:
            self.speed = restr_speed
            print(
                f"Скорость превышена! Разрешенная скорость {restr_speed} км/ч. " +
                f"Текущая скорость: {self.speed} км/ч")
            return True
        return False
    



class TrafficLight:
    colors: dict

    def __init__(self) -> None:
        self.colors = {
            "green": 2.0,
            "yellow": 0.5,
            "red": 1.0
        }

    def switching(self) -> None:
        for i in self.colors:
            print(i)
            sleep(self.colors[i])


def task1():
    cat = Cat()
    cat.name = "Poker"
    cat.color = "Black"
    cat.age = 3
    print(f"{cat.meow()}\n{cat.purring()}\n{cat.sleep()}")


def task2():
    cat = Cat()
    cat.name = "Poker"
    cat.color = "Black"
    cat.age = 3
    print(f"{cat.meow()}\n{cat.purring()}\n{cat.sleep()}")

    apple = Good('apple', price=100, weight=1.5)
    pear = Good('pear', price=120, weight=0.8)
    print(apple)
    print(pear)


def task3():
    car = Car("Black", "BMW", "Sedan", 135.0, "I dunno")
    print(car.start())
    print(car.turn("left"))
    print(car.speed_up(150))
    print(car.speed_down(50))
    print(car.beep())
    print(car.stop())
    print('\n'*2)

    truck = Car("Green", "Samsung", "Truck", 75.0, "Kinda Sorda box")
    print(truck.start())
    print(truck.turn("straight"))
    print(truck.speed_up(12))
    print(truck.speed_down(12))
    print(truck.beep())
    print(truck.stop())


def task4():
    car = Car("Black", "BMW", "Sedan", 135.0, "I dunno")
    print(car.start())
    print(car.turn("left"))
    print(car.speed_up(150))
    print(car.speed_down(50))
    print(car.beep())
    print(car.stop())
    print('\n'*2)

    truck = Car("Green", "Samsung", "Truck", 75.0, "Kinda Sorda box")
    print(truck.start())
    print(truck.turn("straight"))
    print(truck.speed_up(12))
    print(truck.speed_down(12))
    print(truck.speed_up(1))
    print(truck.beep())
    print(truck.stop())


def task5():
    tl = TrafficLight()
    while True:
        tl.switching()
        print()
