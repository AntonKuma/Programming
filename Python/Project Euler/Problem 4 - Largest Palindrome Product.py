global save
save = 0
def balik(c):
    global terbalik
    terbalik = 0
    while c > 0:
        r = c % 10
        c = c // 10
        terbalik = terbalik * 10 + r

for a in range(100, 1000):
    for b in range(100, 1000):
        n = (a) * (b)
        balik(n)
        if n == terbalik:
            if save < n:
                save = n
print('HASIL ',save)
