f = open("input.txt", "r")

m = []

for l in f:
    lettres = l[:-1]
    m.append(lettres)

somme = 0
for i in range(1, len(m)-1):
    for j in range(1, len(m[0])-1):
        if m[i][j] == "A":
            cpt = 0
            for decH in [-1, 1]:
                for decV in [-1, 1]:
                    if m[i+decH][j+decV] == "M" and m[i+(-1*decH)][j+(-1*decV)] == "S":
                        cpt += 1
            if cpt == 2:
                somme += 1
print(somme)