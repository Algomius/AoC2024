next = {"N" : "E",
        "E" : "S",
        "S" : "O",
        "O" : "N"}

depl = {"N" : (-1, 0),
        "E" : (0, +1),
        "S" : (+1, 0),
        "O" : (0, -1)}

def estBoucle(m, pos, direction):
    visite = set()
    while True:
        if (pos[0], pos[1], direction) in visite:
            return True
        visite.add((pos[0], pos[1], direction))

        nextY = pos[0] + depl[direction][0]
        nextX = pos[1] + depl[direction][1]
        if 0 <= nextY < len(m) and 0 <= nextX < len(m[0]):
            if m[nextY][nextX] == '#':
                direction = next[direction]
            else:
                pos = [nextY, nextX]
        else:
            return False
        
f = open("input.txt", "r")
direction = "N"
m = []
dep = None

for l in f:
    m.append(list(l[:-1]))
    if '^' in l:
        dep = [len(m) - 1, l.index('^')]

nbLoop = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] != '#':
            m[i][j] = "#"
            if estBoucle(m, dep[:], direction):
                nbLoop += 1
            m[i][j] = "."

print(nbLoop)