E_betu = 0
D_betu = 0
K_betu = 0
N_betu = 0

parancs = input("Kérem a robot parancsait:")

for i in parancs:
    if i == "E":
        E_betu += 1
    if i == "D":
        D_betu += 1
    if i == "K":
        K_betu += 1
    if i == "N":
        N_betu += 1
print(f"E betűk száma: {E_betu}")
print(f"D betűk száma: {D_betu}")
print(f"K betűk száma: {K_betu}")
print(f"N betűk száma: {N_betu}")

X = 0
Y = 0
for i in parancs:
    if i == "E":
        Y += 1 
    if i == "D":
        Y -= 1
    if i == "K":
        X -= 1
    if i == "N":
        X += 1


print("Egy legrövidebb út parancsszava: " , end="")
if X >= 0:
    for i in range(X):
        print("N", end="")
else:
    for i in range(abs(X)):
        print("K", end="")

if Y >= 0:
    for i in range(Y):
        print("E", end="")
else:
    for i in range(abs(Y)):
        print("D", end="")        

