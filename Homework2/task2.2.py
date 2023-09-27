"""
Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions.
"""
from fractions import Fraction

a, b = map(int, input("Введите первую дробь вида a/b: ").split('/'))
c, d = map(int, input("Введите вторую дробь вида c/d: ").split('/'))


def numerator_res_sum(a1, b1, c2, d2):  # числитель суммы дробей
    return c2 * b1 + a1 * d2


def denominator_res_sum(b1, d2):  # знаменатель суммы дробей
    return b * d


def gcd(m, n):  # наибольший общий делитель для сокращения дроби в результате
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


print("сумма дробей равна: ",
      int(numerator_res_sum(a, b, c, d) / gcd(numerator_res_sum(a, b, c, d), denominator_res_sum(b, d))), "/",
      int(denominator_res_sum(b, d) / gcd(numerator_res_sum(a, b, c, d), denominator_res_sum(b, d))), sep='')


def product_of_fractions_number(a1, b1, c2, d2):
    return (a1 * c2) / (b1 * d2)


print('произведение дробей равно: ', int(a * c / gcd(a * c, b * d)), '/', int(b * d / gcd(a * c, b * d)), sep='')

print('***************************************')
print('проверка:')

num1: Fraction = Fraction(a, b)
num2: Fraction = Fraction(c, d)
print(num1, num2, sep='\n')
print(f'сумма дробей: ', num1 + num2)
# print(num1 - num2)
print(f'произведение дробей: ', num1 * num2)
# print(num1 / num2)
