a=float(input("Введите a (желательно не 0 !!!) ->\t"))
b=float(input("Введите b ->\t"))
c=float(input("Введите c ->\t"))
d=float(input("Введите d ->\t"))
f=float(input("Введите f ->\t"))
if a==0:
    print("Ошибочка:\ta = 0")
else:
    print(abs(a-b*c*d**3+(c**5-a**2)/a+f**3*(a-213)))