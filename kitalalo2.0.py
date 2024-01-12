import random
rejtett_szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]
valasztott_szo = random.choice(rejtett_szavak)

tipp_db = 0
while True:
    tipp = input("Kérem a tippet: ")
    if tipp == "stop":
        break
    tipp_db += 1
    eredmeny = ""

    for i in range(len(rejtett_szavak)):
        if valasztott_szo[i] == tipp[i]:
            eredmeny += tipp[i]
        else:
            eredmeny += "."
    print("Az eredmény:", eredmeny)
    if eredmeny == rejtett_szavak:
        print(f"{tipp_db} tippeléssel sikerült kitalálni.")
        break            

