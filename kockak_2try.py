import random
anni_nyert = 0
panni_nyert = 0
N = 0
dobas =[]
N = int(input("Hány alkalommal legyen feldobás? "))
for i in range(N):
    dobas = [random.randint(1 , 6) for i in range(3)]
    print(f"\n Dobás: {dobas} = {sum(dobas)}", end="       ")
    if sum(dobas) < 10 :
        print ("Nyert: Anni" )
        anni_nyert += 1
    else:
        print("Nyert: Panni")
        panni_nyert += 1
print(f'\nAz összes dobás után Anni {anni_nyert} alkalommal, Panni pedig {panni_nyert} alkalommal nyert.')
    
