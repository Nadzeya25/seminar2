list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 11, 12, 13, 14, 15]
list3 = ['a', 'b', 'c', 'd', 'e', 'f']

current_num = 14
print(list2.index(current_num))  # 4
print(list2[4])  # 14
print(list3[list2.index(current_num)])
