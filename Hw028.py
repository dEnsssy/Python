# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Пример:*
# 2 2
#     4 
a=int(input("Введите A: "))
b=int(input("Введите B: "))

def Sum(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>=b:
        a+=1
        return Sum(a,b-1)
    if a<b:
        b+=1
        return Sum(a-1,b)



print(Sum(a,b))