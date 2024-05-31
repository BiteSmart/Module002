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






*********************************  -= END OF HOMEWORK CONTENTS =-  *********************************
"""