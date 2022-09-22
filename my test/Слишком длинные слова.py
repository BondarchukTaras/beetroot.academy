# if __name__ == '__main__':
for s in [*open(0)][1:]: l = len(s) - 3;
print([s[:-1], s[0] + str(l) + s[-2]][l > 8])