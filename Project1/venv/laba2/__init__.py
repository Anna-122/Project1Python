class SumFunction:
    x1 = input('Введите x: ')

    if len(x1) != 3:
        print('Число не трехзначное')
    else:
        lst = list(map(int, list(x1)))
        first, last = lst[:3], lst[3:]

        if sum(first) == sum(last):
            print( print_digits_sum)


 '''
 input("Введите трехзначное число для суммирования ")

 print("Отлично! Вы ввели трехзначное число")

 input("Введите трехзначное число для суммирования ")
 print("Отлично! Вы ввели трехзначное число")

 print("Суммируем")
'''

#def print_digits_sum(arg1, arg2):
#  print(x1 + x2)








