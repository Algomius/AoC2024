depl = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
diag = [(-1, 1), (-1, -1), (1, -1), (1, 1)]

def calculCout(m, i, j, visite):
    a, g = aireAngle(m, i, j, visite)
    return a * g

def aireAngle(m, i, j, visite):
    visite[i][j] = True
    aire = 1
    angle = 0

    for v in diag:
        if not(0 <= i+v[0] < len(m) or 0 <= j+v[1] < len(m[0])):
            angle += 1
        elif not(0 <= i+v[0] < len(m)):
            if m[i][j+v[1]] != m[i][j]:
                angle += 1
        elif not(0 <= j+v[1] < len(m[0])):
            if m[i+v[0]][j] != m[i][j]:
                angle += 1
        elif m[i+v[0]][j+v[1]] != m[i][j]:
            if (m[i+v[0]][j] != m[i][j] and m[i][j] != m[i][j+v[1]]) or \
                (m[i+v[0]][j] == m[i][j] and m[i][j] == m[i][j+v[1]]):
                angle += 1
        elif m[i+v[0]][j+v[1]] == m[i][j] and m[i+v[0]][j] != m[i][j] and m[i][j+v[1]] != m[i][j]:
            angle += 1


    for x, y in depl:
        if 0 <= i+x < len(m) and 0 <= j+y < len(m[0]):
            if m[i+x][j+y] == m[i][j]: 
                if visite[i+x][j+y] == False:
                    a, g = aireAngle(m, i+x, j+y, visite)
                    aire += a
                    angle += g

    return aire, angle

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

