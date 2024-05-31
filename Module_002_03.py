#####################################################################################
#                                                                                   #
#                                    2024-05-31                                     #
#   2023/09/29 00:00|Домашняя работа по уроку "Стиль кода часть II. Цикл While.""   #
#                                                                                   #
#          https://urban-university.ru/members/courses/course999421818026/          #
#  20230929-0000domasnaa-rabota-po-uroku-stil-koda-cast-ii-cikl-while-845460207601  #
#                                                                                   #
############################ The homework code is below #############################

TASK_STR_LEFT_INDENT = 3  # Indent for task strings with results
task_str_first_column_width = 60  # String length for comment in homework tasks (left part of output)

def e_print(message, result_value):  # Extended print with output format
    print(f'{' ': >{TASK_STR_LEFT_INDENT}}{message: <{task_str_first_column_width}}{result_value}\n')


list_ = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

def iter_loop(list_):
    if not hasattr(list_, '__next__'):
        list_ = iter(list_)
    current_element = next(list_, None)  # Инициализируем первым элементом списка или None, если список пуст
    result = []
    while (current_element is not None) and (current_element >= 0):  # and current_element >= 0:
        try:
            if current_element != 0:
                result.append(current_element)
            current_element = next(list_, None)  # Переход к следующему элементу
        except StopIteration:
            current_element = None  # Если список закончился, устанавливаем текущий элемент в None
    return result

e_print('Printing positive items till first negative: ', iter_loop(list_))


############################# End of the homework code ##############################

"""
*************************************************************************************
|                              -= HOMEWORK CONTENTS =-                              |
*************************************************************************************
2024-05-31

2023/09/29 00:00|Домашняя работа по уроку "Стиль кода часть II. Цикл While."
Цель: применить навыки создания цикла while, а так же применения операторов break и continue.

Задача "Нули ничто, отрицание недопустимо!":
Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список (выход за границу).

Пункты задачи:

    Запишите исходный список в переменную my_list.
    Напишите цикл while с соответствующими задаче условиями.
    Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.


Результат выполнения программы:
Исходные данные:
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

Вывод на консоль:
42
69
322
13
99

Примечания:

    Чтобы перебрать список вам понадобиться обращение по индексу, запишите в отдельную переменную начальное значение - 0.
    Чтобы не выйти за границу списка, в условии цикла while рекомедуется сравнивать текущий индекс и длину списка (функция len()).
    Оператор continue - возвращает вас к условию цикла, игнорируя код после себя, break - прерывает цикл.
    0 - не отрицательное и не положительное число.


Файл с кодом (module_2_3.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.
Успехов!

*************************  -= END OF HOMEWORK CONTENTS =-  **************************
"""