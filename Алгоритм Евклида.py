if __name__ == '__main__':
    print('Введите первое число')
    a = int(input())
    print('Введите второе число')
    b = int(input())
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    print('Наибольшее общее для деления данных чисел', a)
    print("The program is complete")
