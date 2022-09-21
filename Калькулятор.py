print("Введите первое значение")
number_1 = int(input())
print("Введите второе значение")
number_2 = int(input())
print("Введите математический знак. Например: +, -, *, **, /, //, %")
operation = input('''''')
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operation == "-":  # вычитание
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
elif operation == '*':  # умножение
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif operation == "//":  # целочисленое деление
    print('{} // {} = '.format(number_1, number_2))
    print(number_1 // number_2)
elif operation == "**":  # возведение в степень
    print('{} ** {} = '.format(number_1, number_2))
    print(number_1 ** number_2)
elif operation == "%":  # остаток от деления
    print('{} % {} = '.format(number_1, number_2))
    print(number_1 % number_2)
elif operation == "/":  # деление
    print('{} / {} = '.format(number_1, number_2))
    print(number_1/+ number_2)
else:
    print('Не верно введено значение')
