if __name__ == '__main__':
    while True:
        a = [54, 12, 1, 3, 15]
        while len(a) > 0:
            last = a.pop()
            if last % 2 != 0:
                print("No", last)
        else:
            print("Yes", last)
        if len(a) == 0:
            break
    print("The program is complete")