f = open("input.txt", "r")

m = []

for l in f:
    lettres = l[:-1]
    m.append(lettres)

cpt = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "X":
            for decH in [-1, 0, 1]:
                for decV in [-1, 0, 1]:
                    if i+(3*decH) >= 0 and i+(3*decH) < len(m[0]) and j+(3*decV) >= 0 and j+(3*decV) < len(m):
                        if m[i+(1*decH)][j+(1*decV)] == "M" and \
                            m[i+(2*decH)][j+(2*decV)] == "A" and \
                            m[i+(3*decH)][j+(3*decV)] == "S":
                                cpt += 1

print(cpt)