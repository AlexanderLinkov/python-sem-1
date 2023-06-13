n = int(input("Введите размер шоколадки n: "))
m = int(input("Введите размер шоколадки m: "))
k = int(input("Введите количество долек k: "))
s = n * m
if ((s - k) % 2) == 0:
    print('yes')
else:
    print('no')