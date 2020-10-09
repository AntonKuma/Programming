a = 1
b = 2
c = 0
d = 0
while True:
    c = a+b
    a = b
    b = c
    if c > 4000000:
        break
    else:
        if c % 2 == 0:
            d += c
print(d + 2)
