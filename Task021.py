# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def summ(k):
    summa=0
    for i in range(1,k//2+1):
        if k%i==0:
            summa+=i
    return summa

n=int(input("Введите число n: "))
for i in range(n):
    for j in range(i):
        if summ(i)==j and summ(j)==i and i!=j:
            print(f'{i} {j}')





