####################################################################################################
#                                                                                                  #
#                                            2024-05-31                                            #
#   2023/09/28 00:00|Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."    #
#                                                                                                  #
#                 https://urban-university.ru/members/courses/course999421818026/                  #
#  20230928-0000domasnaa-rabota-po-uroku-uslovnaa-konstrukcia-operatory-if-elif-else-585752370454  #
#                                                                                                  #
#################################### The homework code is below ####################################

TASK_STR_LEFT_INDENT = 3  # Indent for task strings with results
task_str_first_column_width = 40  # String length for comment in homework tasks (left part of output)

def e_print(message, result_value):  # Extended print with output format
    print(f'{' ': >{TASK_STR_LEFT_INDENT}}{message: <{task_str_first_column_width}}{result_value}\n')

first = input('Input first number: ')
second = input('Input second number: ')
third = input('Input third number: ')

if first == second == third:
    print('\nTask 1 case found: Throw "3" if all digits are equal.')
    e_print('All digits are equal: ', 3)
elif (first in [second, third]) or (second in [first, third]) or (third in [first, second]):
    print('\nTask 2 case found: Throw "2" if two digits are equal.')
    e_print('Two equal digits found: ', 2)
else:
    print('\nTask 3 case found: Throw "0" if there are no equal digits.')
    e_print('There are no equal digits: ', 0)



##################################### End of the homework code #####################################





"""
****************************************************************************************************
|                                     -= HOMEWORK CONTENTS =-                                      |
****************************************************************************************************
2024-05-31

2023/09/28 00:00|Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
Цель: применить навыки создания условных конструкций и знания операторов if, else, elif / and, or, not.

Задача "Все ли равны?":
На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

Пункты задачи:

    Если все числа равны между собой, то вывести 3
    Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
    Если равных чисел среди 3-х вообще нет, то вывести 0


Пример результата выполнения программы:
Ввод в консоль 1:
123
456
789

Вывод на консоль 1:
0

Ввод в консоль 2:
42
69
42

Вывод на консоль 2:
2

Примечания:

    Помните, что условная конструкция начинается с if.
    Операторы elif и else не могут существовать самостоятельно, они являются продолжением условной конструкции.
    Старайтесь избегать вложенности условий и описывать их, используя операторы or, and и not.
    Самое хорошее решение не только самое быстрое, но ещё и хорошо читаемое!

Файл с кодом (module_2_2.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.

Успехов!

*********************************  -= END OF HOMEWORK CONTENTS =-  *********************************
"""
