print('Угадай число')
my_number=10
user_number=int(input('Введите число : '))
while user_number!=my_number:
    user_number=int(input('Вы не угадали, попробуйте ещё : '))
print('Вы угадали, поздравляю =)')