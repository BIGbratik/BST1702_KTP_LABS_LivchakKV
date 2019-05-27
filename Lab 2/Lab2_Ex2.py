a=['a','r','ar','ra']
print('Дан следующий список, состоящий из строк : ',a)
S=''
for i in range(len(a)):
    if a[i].startswith('r'):
       S=S+a[i]+'  '
print('Все строки, начинающиеся на "r" : ',S) 