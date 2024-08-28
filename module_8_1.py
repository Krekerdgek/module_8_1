# Задание "Программистам всё можно":
def add_everything_up(a, b):
    try:
        print(a + b)
        # ((a.isinteger() or a.isfloat()) and b.isstring()) or ((b.isinteger() or b.isfloat()) and a.isstring()):
    except TypeError:
        print(str(a) + str(b))

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
