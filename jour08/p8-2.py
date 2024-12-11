f = open("input.txt", "r")

m = []
antenne = {}

for l in f:
    lettres = l[:-1]
    m.append(list(lettres))
    for i in range(len(lettres)):
         if lettres[i] != ".":
            if lettres[i] not in antenne:
                antenne[lettres[i]] = []
            antenne[lettres[i]].append((len(m)-1, i)) 

loc = []

for (l, pos) in antenne.items():
    for i in range(len(pos)-1):
        for j in range(i+1, len(pos)):
            ecarty = pos[i][0] - pos[j][0]
            ecartx = pos[i][1] - pos[j][1]

            testAjout = True
            indice = 0

            while testAjout:
                testAjout = False

                if 0 <= pos[i][1] + (ecartx*indice) < len(m[0]) and 0 <= pos[i][0] + (ecarty*indice)  < len(m):
                    if (pos[i][0]+(ecarty*indice), pos[i][1]+(ecartx*indice)) not in loc:
                        loc.append((pos[i][0]+(ecarty*indice), pos[i][1]+(ecartx*indice)))
                    testAjout = True
                if 0 <= pos[j][1] - (ecartx * indice) < len(m[0]) and 0 <= pos[j][0] - (ecarty * indice) < len(m):
                    if (pos[j][0]-(ecarty*indice), pos[j][1]-(ecartx*indice)) not in loc:
                        loc.append((pos[j][0]-(ecarty*indice), pos[j][1]-(ecartx*indice)))
                    testAjout = True

                indice += 1


print(len(loc))