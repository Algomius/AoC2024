fic = open("input.txt", "r")

ordre = True
somme = 0
ordList = []

for ligne in fic:
    ligne = ligne[:-1]
    if ligne == "":
        ordre = False
    elif ordre:
        ordList.append((int(ligne[0:2]),int(ligne[3:5])))
    else:
        feuilles = [int(x) for x in ligne.split(",")]
        test = True
        change = True
        while change:
            change = False
            for premier, second in ordList:
                if premier in feuilles and second in feuilles:
                    indPremier = feuilles.index(premier)
                    indSecond = feuilles.index(second)
                    if indPremier > indSecond:
                        test = False
                        feuilles[indPremier], feuilles[indSecond] = feuilles[indSecond], feuilles[indPremier]
                        change = True
        if not test:
            somme += feuilles[len(feuilles) // 2]

print(somme)
