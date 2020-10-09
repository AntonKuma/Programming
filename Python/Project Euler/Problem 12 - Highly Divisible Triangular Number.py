import math, time

t_awal = time.time()
minimal = 2**4 * 3**4 * 5**4 * 7 * 11
bil_segi3 = 0
count = 1

#CEK bil_segi3 terdekat
while bil_segi3 <= minimal:
    bil_segi3 += count
    if bil_segi3 == minimal:
        break
    count += 1

#CEK pembagi
while True:
    n_pembagi = 2
    bil_segi3 += count
    akar = int(math.sqrt(bil_segi3)) + 1
    print(count, bil_segi3, end = " --> ")
    for i in range(2,bil_segi3):
        if bil_segi3 % i == 0:
            print(bil_segi3 // i, end = ", ")
            n_pembagi += 1
    print("1", end = "-- ")
    print("PEMBAGI",n_pembagi)
    if n_pembagi >= 500:
        break
    count += 1

print()
print("=" * 10)
print(bil_segi3, count)
print(time.time() - awal, "s")
