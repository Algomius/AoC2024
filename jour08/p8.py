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

            if 0 <= pos[i][1] + ecartx < len(m[0]) and 0 <= pos[i][0] + ecarty  < len(m)  and (pos[i][0]+ecarty, pos[i][1]+ecartx) not in loc:
                loc.append((pos[i][0]+ecarty, pos[i][1]+ecartx))
            if 0 <= pos[j][1] - ecartx < len(m[0]) and 0 <= pos[j][0] - ecarty < len(m)  and (pos[j][0]-ecarty, pos[j][1]-ecartx) not in loc:
                loc.append((pos[j][0]-ecarty, pos[j][1]-ecartx))


print(len(loc))