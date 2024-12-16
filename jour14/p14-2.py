f = open("input.txt", "r")
largeurPiece = 103
hauteurPiece = 101

depart = []
vitesse = []
for l in f:
    valeur = l[:-1].split(" ")
    depart.append([int(x) for x in valeur[0][2:].split(",")])
    vitesse.append([int(x) for x in valeur[1][2:].split(",")])

minimum = float('Inf')
minPeriod = -1
for etapes in range(10000):
    arrivee = set()
    for i in range(len(depart)):
        arrivee.add(((depart[i][0]+(etapes * vitesse[i][0]))%hauteurPiece, (depart[i][1]+(etapes * vitesse[i][1]))%largeurPiece))
    if len(arrivee) == len(depart):
        minPeriod = etapes

print(minPeriod)