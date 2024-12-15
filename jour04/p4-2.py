fic = open("input.txt", "r")

grille = []

for ligne in fic:
	grille.append(ligne[:-1])
	
cpt_xmas = 0

for i in range(len(grille)):
     for j in range(len(grille[0])):
        if grille[i][j] == "A":
            cpt_diag = 0
            for decH in [-1, 1]:
                for decV in [-1, 1]:
                    if 0 <= i+decV < len(grille) and 0 <= j+decH < len(grille[0]) and \
                        0 <= i+(-1*decV) < len(grille) and 0 <= j+(-1*decH) < len(grille[0]):
                        if grille[i+decV][j+decH] == "M" and grille[i+(-1*decV)][j+(-1*decH)] == "S":
                            cpt_diag = cpt_diag + 1
            if cpt_diag == 2:                
                cpt_xmas += 1 
print(cpt_xmas) 