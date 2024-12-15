f = open("input.txt", "r")

somme = 0
coordA = None
coordB = None
coordX = None
coutA = 3
coutB = 1

for x in f:
    if "Button A:" in x:
        ligne = x[:-1].split(":")
        valeurs = ligne[1].split(",")
        coordA = (int(valeurs[0][3:]),int(valeurs[1][3:]))
    elif "Button B:" in x:
        ligne = x[:-1].split(":")
        valeurs = ligne[1].split(",")
        coordB = (int(valeurs[0][3:]),int(valeurs[1][3:]))
    elif "Prize:" in x:
        ligne = x[:-1].split(":")
        valeurs = ligne[1].split(",")
        coordX = (int(valeurs[0][3:]),int(valeurs[1][3:]))
        min = float('inf')
        for i in range(101):
            for j in range(101):
                if (i * coordA[0])+ (j * coordB[0]) == coordX[0] and (i * coordA[1]) + (j * coordB[1]) == coordX[1] and min > (i * coutA) + (j * coutB):
                    min = (i*coutA) + (j*coutB)

        if min != float('inf'):
            somme += min

print(somme)


