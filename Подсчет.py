if __name__ == '__main__':
    #     a = [5, 1, 2, 5, 1, 4, 5, 3, 1, 0, 4]
    #     count = [0] * 6
    #     for i in a:
    #         count[i] += 1
    # print(count)
    # for i in range(6):
    #     if count[i] > 0:
    #         print((str(i) + " ") * count[i], end="", )
    # print()
    # print("The program is complete")

    # s = "vxmv;sa// JJDSmn  YYY {PJDS 53151"
    # letters = [0] * 26
    # for i in s.lower():
    #     if i >= "a" and i <= "z":
    #         nomer = ord(i) - 97
    #         letters[nomer] += 1
    # for i in range(26):
    #     if letters[i] > 0:
    #         print(chr(i + 97), letters[i])

    a = []
    import random

    for i in range(10):
        a.append(random.randint(-10, 10))
    count = [0] * 21
    for i in a:
        count[i + 10] += 1
    print(a)
    for i in range(21):
        print(i - 10, count[i])
