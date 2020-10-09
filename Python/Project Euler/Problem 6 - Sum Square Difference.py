SoSq = 0
SqoS = 0
for a in range(100):
    SoSq = SoSq + ((a + 1) * (a + 1))
    SqoS += (a + 1)
print(SoSq, SqoS * SqoS, SqoS * SqoS - SoSq)
