s='ab1cd34gjdnsuv4'
print('Изначальная строка : ',s)
s_chi=''
s_bu=''
n=len(s)
for i in range(n):
    if (ord(s[i])>=48 and ord(s[i])<=57) :
        s_chi+=s[i]
    elif (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122) or ord(s[i])==1025 or ord(s[i])==1105 or (ord(s[i])>=1040 and ord(s[i])<=1103):
        s_bu+=s[i]
print('Строка чисел : ',s_chi)
print('Строка букв : ',s_bu)