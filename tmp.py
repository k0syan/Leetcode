n = 38

c = 0
while True:
    a = 0
    while n != 0:
        a += n % 10
        n = n // 10
    c += 1
    n = a
    if n // 10 == 0:
        break
print(c)