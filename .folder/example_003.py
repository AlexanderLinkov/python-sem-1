n = int(input("Введите номер Вашего билета: "))
total1 = 0
total2 = 0
for i in range(3):
    total1 += n % 10
    n //= 10
for j in range(3):
    total2 += n % 10
    n //= 10
if total1 == total2:
    print('yes')
else:
    print('no')