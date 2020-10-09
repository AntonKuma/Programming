import math, time
awal = time.time()
prima = 3
jumlah = 2
while prima <= 2000000:
    akar = int(math.sqrt(prima)) + 1
    for i in range(2, akar):
        if prima % i == 0:
            break
    else:
        jumlah += prima
        print(prima, jumlah)
    prima += 2
print(time.time()-awal)
