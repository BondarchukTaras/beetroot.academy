if __name__ == '__main__':
    a = [43, 65, 3, 54, 43, 10, 50, 65, 10, 54]
    b=[]
    for i in a:
        if not i in b:
            b.append(i)
print(a)
print(b)
