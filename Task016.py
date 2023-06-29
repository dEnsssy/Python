# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def Prostoe(n):
    for i in range(2,n):
        if n%i==0:
            return "Составное"
    return "Простое"
n=int(input('Число: '))
print(Prostoe(n))