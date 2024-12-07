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
        test = True
        for dep, arr in ordList:
            if dep in feuilles and arr in feuilles:
                if feuilles.index(dep) > feuilles.index(arr):
                    test = False

        if test:
            somme += feuilles[len(feuilles)//2]


print(somme)