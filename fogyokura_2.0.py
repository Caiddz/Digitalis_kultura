hetek_szama = int(input("Hetek száma="))
cél = float(input("Elérni kívánt testtömeg (kg)="))
tömeg = []
for i in range(hetek_szama):
    tömeg.append(float(input(f"{i + 1}. héten=")))
cel_elerve = 0
for i in range(hetek_szama):
    if tömeg[i] <= cél: 
        cel_elerve = i + 1
        break
if cel_elerve > 0:
    print(f"Mari néni {cel_elerve}. héten érte el célját.")      
else:
    print("Sajnos Mari néni nem érte el a célját.")
visszafogyas_szam = 0
for i in range(1,hetek_szama):
    if tömeg[i] > tömeg[i - 1]:
        visszafogyas_szam += 1
print(f" A tömege {visszafogyas_szam} esetben nőtt eggyik hétről a másikra.")    

