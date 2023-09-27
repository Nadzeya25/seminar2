"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
 Функцию hex используйте для проверки своего результата.
"""

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 11, 12, 13, 14, 15]
list3 = ['a', 'b', 'c', 'd', 'e', 'f']

num = int(input('Введите число'))
print(f'так нужно получить - ', hex(num))
res = ''
while num:
    current_num = num % 16
    if current_num in list1:
        res = f'{current_num}' + res
        num //= 16
    elif current_num in list2:
        res = f'{list3[list2.index(current_num)]}' + res
        num //= 16

print(f'так получилось - ', res)

