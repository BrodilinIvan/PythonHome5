"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def many_num(n=0, rezult_left=0, rezult_right=0):
    """
    Данная функция many_num проверяет равенство для множества натуральных чисел
     в выражении 1+2+...+n = n(n+1)/2.
    В данной функции используются три переменных: n - любое натуральное число,
    которое запрашивается у пользователя, rezult_left - результат вычисления
    левой части, rezult_right - результат вычисления правой части выражения.
    """
    if n == 0:
        try:
            n = int(input('Введите целое число, которое > 0: '))
            if n < 1:
                print('Введено некорректное значение! Повторите ввод!')
                many_num(n=0)
        except ValueError:
            print('Введено некорректное значение! Повторите ввод!')
            many_num(n=0)
        rezult_right = int((n * (n + 1)) / 2)
        many_num(n=n, rezult_right=rezult_right)
    else:
        rezult_left = rezult_left + n
        if n == 1:
            return print(f'Результат вычисления \n '
                         f'Левой части выражения: {rezult_left} \n'
                         f'Правой части выражения: {rezult_right}')
        many_num(n - 1, rezult_left=rezult_left, rezult_right=rezult_right)


many_num()
