n = int(input("Введите трехзначное число: "))
total = 0
for i in range(3):
    total += n % 10
    n //= 10
print(total)