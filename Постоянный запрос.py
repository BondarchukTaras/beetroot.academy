if __name__ == '__main__':
    print('Введите число')
while True:
    n = input()
    i = 1
    if n == 'exit':
        break
        print("The program is complete")
    while i <= int(n) // 2:  # все делители на 2
        if int(n) % i == 0:
            print(i, end=" ")
        i += 1
    print(n, '\n Введите число или exit завершения')
