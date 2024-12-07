f = open("input.txt", "r")

order = True
ordList = []

somme = 0

for l in f:
    ligne = l[:-1]
    if ligne == "":
        order = False
    elif order:
        ordList.append((int(ligne[0:2]), int(ligne[3:5])))
    else:
        feuilles = [ int(x) for x in ligne.split(',')]
        isValid = True
        change = True
        while change:
            change = False
            for dep, arr in ordList:
                if dep in feuilles and arr in feuilles:
                    indexDep = feuilles.index(dep)
                    indexArr = feuilles.index(arr)
                    if indexDep > indexArr:
                        isValid = False
                        feuilles[indexDep],feuilles[indexArr] = feuilles[indexArr], feuilles[indexDep] 
                        change = True

        if not isValid:
            somme += feuilles[len(feuilles)//2]


print(somme)