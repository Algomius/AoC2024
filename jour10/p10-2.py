f = open("input.txt", "r")

def nbChemin(m, x, y, val):
    lst9 = []
    
    if val == 9:
        return [(x, y)]

    for deltaX, deltaY in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        if 0 <= x+deltaX < len(m[0]) and 0 <= y+deltaY < len(m):
            if m[x+deltaX][y+deltaY] == val + 1:
                lst9 += nbChemin(m, x+deltaX, y+deltaY, val+1)

    return lst9


m = []
for x in f:
    m.append([int(e) for e in list(x[:-1])])

somme = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 0:
            print(i, j, nbChemin(m, i, j, 0))
            somme += len(nbChemin(m, i, j, 0))
print(somme)


