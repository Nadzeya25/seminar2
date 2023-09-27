# ___________________isinstance_______________________проверка типа объекта

x = 1
print(isinstance(x, int))
# True
x = [1, 2, 3]
print(isinstance(x, list))
# True
x = (1, 2, 3)
print(isinstance(x, tuple))
# True
# Проверим, является ли строка 'Hello' одним из типов, описанных в параметре type
print(isinstance('Hello', (float, int, str, list, dict, tuple)))
# True
d = False
print(isinstance(d, int))
# True --потому что булевы значения - это подтип числовых значений


