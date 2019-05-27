a=['a','1','a345v','123456789']
print('Задан следующий список :\t',a)
S=''
for i in range(len(a)):
    A=a[i]
    j=0
    for j in range(len(A)):
        if A[j]=='1' or A[j]=='3' or A[j]=='5' or A[j]=='7' or A[j]=='9':
            S=S+A[j]
print('Строка всех нечётных цифр списка :\t',S)