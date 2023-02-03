"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def func_sum(first_num=1, rezult=0, count_num=0, count_num_copy=0):
    """
    Данная функция складывает последовательность чисел, начиная с 1, которая
    содержится в переменной first_num и сохраняется в переменной rezult.
    Последовательность чисел создается делением переменной first_num на -2 и
    сохраняется в ней же, количество операций запрашиваем у пользователя и
    сохраняем в count_num. В count_num_copy считаем количество элементов.
    """
    if count_num == 0:
        try:
            count_num = int(input('Введите количество элементов: '))
            if count_num < 1:
                print('Введено некорректное значение!Повторите ввод!')
                func_sum(first_num=1, rezult=0, count_num=0, count_num_copy=0)
        except (ValueError, RecursionError):
            print('Введено некорректное значение!Повторите ввод!')
            func_sum(first_num=1, rezult=0, count_num=0, count_num_copy=0)
        func_sum(first_num=1, rezult=0, count_num=count_num, count_num_copy=0)
    else:
        rezult = rezult + first_num
        count_num -= 1
        count_num_copy += 1
        if count_num == 0:
            print(f'Количество элементов: {count_num_copy}, '
                  f'их сумма: {rezult}')
            return
        else:
            first_num /= -2
            func_sum(first_num, rezult, count_num, count_num_copy)

func_sum()
