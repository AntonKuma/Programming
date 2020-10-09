import time

awal = time.time()
x = 2
y = 2
path_count = 0

while x != 0:
    b = y
    while b != 0:
        path_count += 1
        b -= 1
    x -= 1

print("Number of routes =", path_count)
print("Time elapsed", time.time() - awal, "s")
