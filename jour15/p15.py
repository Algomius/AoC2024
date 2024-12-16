depl = {"^" : (0, -1),
        "v" : (0, 1),
        "<" : (-1, 0),
        ">" : (1, 0)
        }

f = open("input.txt", "r")

estGrille = True
grille = []
position = None
for l in f:
    l = l[:-1]
    if l == "":
        estGrille = False
    elif estGrille:
        if "@" in l:
            position = [l.find("@"), len(grille)]
            l = l.replace("@", ".")
        grille.append(list(l))
    else:
        for e in l:
            if grille[position[1] + depl[e][1]][position[0] + depl[e][0]] == ".":
                position = [position[0] + depl[e][0],position[1] + depl[e][1]]
            elif grille[position[1] + depl[e][1]][position[0] + depl[e][0]] == "O":
                nb_depl = 1
                while grille[position[1] + (nb_depl * depl[e][1])][position[0] + (nb_depl* depl[e][0])] == "O":
                    nb_depl += 1

                if grille[position[1] + (nb_depl * depl[e][1])][position[0] + (nb_depl* depl[e][0])] == ".":
                    grille[position[1] + (nb_depl * depl[e][1])][position[0] + (nb_depl* depl[e][0])], grille[position[1] + depl[e][1]][position[0] + depl[e][0]] = \
                    grille[position[1] + depl[e][1]][position[0] + depl[e][0]], grille[position[1] + (nb_depl * depl[e][1])][position[0] + (nb_depl* depl[e][0])]
                    position = [position[0] + depl[e][0],position[1] + depl[e][1]]

somme = 0
for i in range(len(grille)):
    for j in range(len(grille[0])):
        if grille[i][j] == "O":
            somme += (100 * i) + j

print(somme)
        

