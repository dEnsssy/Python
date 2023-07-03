# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

startList=[]
resultList=[]

n=int(input("Введите длину массива: "))
first=int(input("Введите первую границу диапозона: "))
second=int(input("Введите вторую границу диапозона: "))
if first>second: # По сути не обязательная проверка,но так точно first-левая граница
    first,second=second,first

for _ in range(n):
    startList.append(randint(-15,15))
for i in range(len(startList)):
    if startList[i]>=first and startList[i]<=second:
        resultList.append(i)
print(startList)
print(resultList)