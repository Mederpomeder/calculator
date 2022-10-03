a = int(input('Введите первое число: '))

b = int(input('Введите второе число: '))

c = str(input('Выберите операцию из следующих:+-*/**//:'))

if c == '+':
    d = a + b
    print(f'Ответ:{d}')
elif c == '-':
    d = a - b
    print(f'Ответ:{d}')
elif c == '*':
    d = a * b
    print(f'Ответ: {d}')
elif c == '/':
    d = a / b
    print(f'Ответ: {d}')
elif c == '**':
    d = a ** b
    print(f'Ответ: {d}')
elif c == '//':
    d = a // b
    print(f'Ответ: {d}')
else:
    print('Ответ: Данной операции нет в системе')