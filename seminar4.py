# task 1. Вычислить число c заданной точностью d

# d = int(input('Количество символов после запятой вещественного числа: '))
# n = float(input('Введите число: '))
# print(round(n, d))


# task 2. Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите число: '))
# some_list = []
# for i in range(2, n//2+1):
#     if n % i == 0:
#         for j in range(2, i//2+1):
#             if i % j == 0:
#                 break
#         else:
#             some_list.append(i)
# print(some_list)


# task 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

# count = int(input('Количество чисел в проверяемой последовательности: '))
# some_list = []
# for _ in range(count):
#     n = int(input('Вводите числа по одному: '))
#     some_list.append(n)
# unique_list =[]
# for i in some_list:
#     if i in unique_list:
#         continue
#     else:
#         unique_list.append(i)
# print(unique_list)


# count = int(input('Количество чисел в проверяемой последовательности: '))
# some_list = []
# for _ in range(count):
#     n = int(input('Вводите числа по одному: '))
#     some_list.append(n)

# print(list(set(some_list)))


# task 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# from encodings import utf_8_sig
# import random
# k = int(input('Введите степень k: '))
# polin_list = [random.randint(0, 101) for _ in range(k+1)]
# print(polin_list)
# with open('polinomial.txt', 'w', encoding = 'utf-8') as fail:
#     for i in range(len(polin_list)):
#         if k-i !=1 and k-i != 0:
#             fail.write(f'{polin_list[i]}x^{k-i} + ')
#         elif k - i ==1:
#             fail.write(f'{polin_list[i]}x + ')
#         elif k - i == 0:
#             fail.write(f'{polin_list[i]} = 0')
        
        

