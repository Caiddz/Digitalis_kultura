Taj_szam = input("Kérem a TAJ-számot: ")
ellenorzo_szam = int(Taj_szam[-1])
print(f"Az ellenőrzőszámjegy: {ellenorzo_szam}")
osszeg = 0
for i in range(8):
    szamjegy = int(Taj_szam[i])
    pozicio = i + 1
    if pozicio % 2 == 1:  
        osszeg += szamjegy * 3
    else:
        osszeg += szamjegy * 7
print(f"A szorzatok összege: {osszeg}")

if osszeg % 10 == ellenorzo_szam:
    print("Helyes szám!")
else:
    print("Hibás szám!")

