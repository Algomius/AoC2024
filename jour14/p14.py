f = open("input.txt", "r")
largeurPiece = 103
hauteurPiece = 101
etapes = 100

cpt = [0, 0, 0, 0]
for l in f:
    valeur = l[:-1].split(" ")
    depart = [int(x) for x in valeur[0][2:].split(",")]
    vitesse = [int(x) for x in valeur[1][2:].split(",")]

    arrivee = [(depart[0]+(etapes * vitesse[0]))%hauteurPiece, (depart[1]+(etapes * vitesse[1]))%largeurPiece]
    if arrivee[0] < hauteurPiece // 2 and arrivee[1] < largeurPiece // 2:
        cpt[0] += 1
    elif hauteurPiece //2 < arrivee[0] and arrivee[1] < largeurPiece // 2:
        cpt[1] += 1
    elif arrivee[0] < hauteurPiece // 2 and largeurPiece // 2 < arrivee[1]:
        cpt[2] += 1
    elif hauteurPiece //2 < arrivee[0] and largeurPiece // 2 < arrivee[1]:
        cpt[3] +=1 

print(cpt[0]* cpt[1]* cpt[2]* cpt[3])