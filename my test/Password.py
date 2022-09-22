if __name__ == '__main__':
    print("Ведите Пароль")
    p = "Пароль"
    i = input()
    while i != p:
        print("No")
        i = input()
    else: i = p
    print("Welcome")

