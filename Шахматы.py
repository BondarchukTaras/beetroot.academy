if __name__ == '__main__':
    print('Введите результаты партий')
    s=input()
    #s = ('ADAAAA')
    Anton = s.count("A")
    Danik = s.count('D')
    if Anton > Danik:
        print("Anton")
    elif Anton < Danik:
        print("Danik")
    else:
        Anton == Danik
        print("Friendship")
print('игр было', + len(s))