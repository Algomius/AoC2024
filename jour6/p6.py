f = open("input.txt", "r")

next = {"N" : "E",
        "E" : "S",
        "S" : "O",
        "O" : "N"}

depl = {"N" : (-1, 0),
        "E" : (0, +1),
        "S" : (+1, 0),
        "O" : (0, -1)}

direction = "N"
nb_cases = 1

m = []
pos = None

for l in f:
    ligne = l[:-1]
    m.append(list(l))
    if '^' in l:
        pos = [len(m) - 1, l.index('^')]

end = False
m[pos[0]][pos[1]] = 'V'
while not end:
    nextY = pos[0] + depl[direction][0] 
    nextX = pos[1] + depl[direction][1]
    if 0 <= nextY < len(m) and 0 <= nextX < len(m[0]):
        if m[nextY][nextX] == '#':
            direction = next[direction]
        else:
            pos = [nextY, nextX]
            if m[nextY][nextX] == '.':
                nb_cases += 1
                m[nextY][nextX] = 'V'
    else:
        end = True 

print(nb_cases)

