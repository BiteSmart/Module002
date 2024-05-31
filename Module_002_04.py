##########################################################################################################
#                                                                                                        #
#                                               2024-05-31                                               #
#    2023/09/30 00:00|Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле""    #
#                                                                                                        #
#                    https://urban-university.ru/members/courses/course999421818026/                     #
#  20230930-0000domasnaa-rabota-po-uroku-cikl-for-elementy-spiska-poleznye-funkcii-v-cikle-887423494326  #
#                                                                                                        #
####################################### The homework code is below #######################################

TASK_STR_LEFT_INDENT = 0  # Indent for task strings with results
task_str_first_column_width = 20  # String length for comment in homework tasks (left part of output)

def e_print(message, result_value):  # Extended print with output format
    print(f'{' ': >{TASK_STR_LEFT_INDENT}}{message: <{task_str_first_column_width}}{result_value}\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)

e_print('Primes are: ', primes)
e_print('Not primes are: ', not_primes)

######################################## End of the homework code ########################################

"""
**********************************************************************************************************
|                                        -= HOMEWORK CONTENTS =-                                         |
**********************************************************************************************************
2024-05-31

2023/09/30 00:00|Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
Цель: закрепить навык решения задач при помощи цикла for, применив знания об основных типах данных.

Задача "Всё не так уж просто":
Дан список чисел  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Испольуя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:

    Создайте пустые списки primes и not_primes.
    При помощи цикла for переберите список numbers.
    Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
    Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
    В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения перменной is_prime после проверки (True - в prime, False - в not_prime).
    Выведите списки primes и not_primes на экран(в консоль).


Пример результата выполнения программы:
Исходный код:
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Вывод на консоль:
Primes: [2, 3, 5, 7, 11, 13]
Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
Примечания:

    Учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
    Для проверки на простоту числа вам нужно убедиться, что выбранное число не делиться ни на что в диапазоне от 2 до этого числа(не включительно).
    Попробуйте оптимизировать(ускорить) процесс выяснения простоты числа при помощи оператора break, когда найдёте делитель. (Не обязательно)
    Переменные меняющее своё булевое состояние на противоположное в процессе проверки, как is_prime, в кругах разработчиков называются перменными-флагами(flag).


Файл с кодом (module_2_4.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.
Успехов!

************************************  -= END OF HOMEWORK CONTENTS =-  ************************************
"""