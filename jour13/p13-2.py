import numpy as np

f = open("input.txt", "r")

somme = 0
coordA = None
coordB = None
coordX = None
coutA = 3
coutB = 1
ajout = 10000000000000 

for x in f:
    if "Button A:" in x:
        ligne = x[:-1].split(":")
        valeurs = ligne[1].split(",")
        coordA = (int(valeurs[0][3:]),int(valeurs[1][3:]))
    elif "Button B:" in x:
        ligne = x[:-1].split(":")
        valeurs = ligne[1].split(",")
        coordB = (int(valeurs[0][3:]),int(valeurs[1][3:]))
    elif "Prize:" in x:
        ligne = x[:-1].split(":")
        valeurs = ligne[1].split(",")
        coordX = (int(valeurs[0][3:]) + ajout,int(valeurs[1][3:]) + ajout)
        # Utilisation de la résolution des système d'équation avec des matrice -  Ca ne marche pas, les solutions qui devraient marcher 
        # ne sont pas considérées comme entières
        #matA = np.array([[coordA[0], coordB[0]],[coordA[1], coordB[1]]])
        #matB = np.array([[coordX[0]],[coordX[1]]])
        
        #sol = np.linalg.solve(matA, matB)
        #if indice == 11:
        #    print("Solution : ", sol )
        a = (coordX[0]*coordB[1] - coordX[1]*coordB[0]) / (coordA[0]*coordB[1] - coordA[1]*coordB[0])
        b = (coordX[1]*coordA[0] - coordX[0]*coordA[1]) / (coordA[0]*coordB[1] - coordA[1]*coordB[0])
        if a == int(a) and b == int(b):
            somme += int((a*coutA) + (b*coutB))

print(somme)


