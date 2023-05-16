def calculator(n1, n2, oper):
    print(eval(f"{n1}{oper}{n2}"))
    exec(f'print({n1}{oper}{n2})')


s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ',
     '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']


def filtering():
    global s
    cap_s = list(map(lambda data: data.capitalize(), s))
    print(*cap_s)


def honest(data):
    return list(filter(lambda x: x % 2 == 0, data))


def cesar():
    line = input()
    cesar_line: str = ''
    for i in line:
        cesar_line += chr(ord(i) + 3)
    return cesar_line


def countdown(data):
    data = sorted(data, reverse=True)
    for i in data:
        print(i)
    print("Пуск")


def alphabet():
    lch = [chr(x) for x in range(ord('a'), ord('z'))]
    hch = [chr(x) for x in range(ord('A'), ord('Z'))]
    alphabet = hch + lch
    al_dict = dict()
    for i in alphabet:
        al_dict[i] = ord(i)
        print(f'{ord(i)} - {i}')

    print(al_dict)


def decorator(my_decorator):
    def get_name() -> str:
        name = input('Введите имя: ')
        my_decorator(name)
        return name
    return get_name


def greeting(name):
    print(f"Привет, {name}")


def html(my_decorator):
    def parag(field) -> str:
        return f"<p>{my_decorator(field)}</p>"
    return parag


@html
def render_input(field):
    return f'<input id="id_{field}" name="{field}">'


print(render_input("login"))