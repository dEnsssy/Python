# 1. Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.

# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

number=int(input("Введите число: "))

def reverse_func(num:int):
    if num==0:
        return ''
    char = input("Введите что-то: ")
    return reverse_func(num-1)+char

print(reverse_func(number))
