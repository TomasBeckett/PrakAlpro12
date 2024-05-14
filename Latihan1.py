def anggota(t):
    return all(x == t[0] for x in t)

tA = (90, 90, 90, 90)
tB = (90, 90, 91, 90)
hasil1 = anggota(tA)
hasil2 = anggota(tB)
print(hasil1)
print(hasil2) 

