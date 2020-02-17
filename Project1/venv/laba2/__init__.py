def print_digits_sum(arg1, arg2):
    print('Суммируем введенные числа')
    return int(arg1) + int(arg2)


class SumFunction:
    x1 = input('Введите x: ')
    if len(x1) != 3:
        print('Число не трехзначное')
    else:
        print('Число явяется трехзначным')
        lst = list(map(int, list(x1)))
        first, last = lst[:3], lst[3:]
        print(sum(first))
        print(sum(last))

        if sum(first) == sum(last):
            print(print_digits_sum)


print('Завершение работы программы')
