import random
s=''
k=0
while len(s)!=8:
    a=random.randint(48,1105)
    if (a>=48 and a<=57):
        k=1
        s+=chr(a)
    else:
        if (a>=65 and a<=90) or (a>=97 and a<=122) or a==1025 or a==1105 or (a>=1040 and a<=1103):
            s+=chr(a)
if k==0:
    a=random.randint(0,7)
    if a==0:
        s=str(random.randint(0,9))+s[1:]
    else:
        if a==7:
            s=s[:6]+str(random.randint(0,9))
        else:
            s=s[:(a-1)]+str(random.randint(0,9))+s[(a+1):]
print('Случайно сгенерированная строка : ',s) 