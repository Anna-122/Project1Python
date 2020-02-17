x1 = input('Введите x1: ')
if len(x1) != 3:
    print('Число не трехзначное')
else:
    lst = list(map(int, list(x1)))
    first, last = lst[:3], lst[3:]
    print('Отлично')

x2 = input('Введите x2: ')
if len(x2) != 3:
    print('Число не трехзначное')
else:
    lst = list(map(int, list(x2)))
    first, last = lst[:3], lst[3:]
    print('Отлично')


def print_digits_sum(m1, m2):
    print('Вызвана функция print_digits_sum, суммируем введенный числа ' + m1 + " и " + m2)
    return int(m1) + int(m2)


# явное преобразование типа функцией str() используется т.к. конкатенация int со string невозможна в питон
print('Результат суммирования равен ' + str(print_digits_sum(x1, x2)))
