prima = 3
count = 2
#print('1 2')
while count <= 10001:
    for i in range(2, prima):
        if i < prima and prima % i == 0:
            print(prima, i)
            break
    else:
        print (count, prima)
        count += 1
    prima += 2
