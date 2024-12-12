depl = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

def calculCout(m, i, j, visite):
    a, p = airePeri(m, i, j, visite)
    return a * p

def airePeri(m, i, j, visite):
    visite[i][j] = True
    aire = 1
    perimetre = 0
    for x, y in depl:
        if 0 <= i+x < len(m) and 0 <= j+y < len(m[0]):
            if m[i+x][j+y] == m[i][j]: 
                if visite[i+x][j+y] == False:
                    a, p = airePeri(m, i+x, j+y, visite)
                    perimetre += p
                    aire += a
            else:
                perimetre += 1
        else:
                perimetre += 1

    return aire, perimetre

f = open("input.txt", "r")

m = []
for x in f:
    m.append(list(x[:-1]))

visite = [[False for _ in range(len(m[0]))] for _ in range(len(m))]

somme = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if visite[i][j] == False:
            somme += calculCout(m, i, j, visite)

print(somme)

