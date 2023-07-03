def summ(k):
    summa=0
    for i in range(1,k//2+1):
        if k%i==0:
            summa+=i
    return summa

n=int(input("Введите число n: "))
for i in range(1,n):
    j=summ(i)
    if i<j<=n and i==summ(j):
        print(f'{i} {j}')