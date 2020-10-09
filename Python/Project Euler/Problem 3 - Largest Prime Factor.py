n = 600851475143
i = 2
#print('i=', i)
while i * i <= n:
    if n % i:
        i += 1
#        print('i=',i)
    else:
        n //= i
print('n=',n)
