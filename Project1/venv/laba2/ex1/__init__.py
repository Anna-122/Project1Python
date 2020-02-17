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

print('Суммируем')


def print_digits_sum(x1, x2):
    return (x1 + x2)
    result=(x1+x2)

    print(result)
