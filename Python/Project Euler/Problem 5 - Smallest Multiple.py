global a
a = 2520
while True:
#    print(a)
    for i in range(2, 101):
        if a%i == 0:
            if i == 20:
                print(i, a)
                exit()
        else:
            a += 2520
            break
