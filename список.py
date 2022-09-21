
s = '123456789'
print(s)
print(s[::-1])  # наоборот
print(s[1::2])  # четные
print(s[::2])  # не четные
print(s[1:6:2])  # с/по/интервал
s = s[:4] + '0' + s[5:]
print(s)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
st = set(a)  # множество из саписка а
print(st)
print(len(st) == len(a))
