fic = open("input.txt", "r")

somme = 0
testCumul = True

for ligne in fic:
    for indice in range(len(ligne)):
        if ligne[indice:indice+4] == "mul(" and testCumul == True:
            n1 = 0
            taille = 4
            while '0' <= ligne[indice + taille] <= '9':
                n1 = n1 * 10 + int(ligne[indice + taille])
                taille += 1

            if (ligne[indice + taille] == "," and n1 < 1000):
                taille += 1
                n2 = 0
                while '0' <= ligne[indice + taille] <= '9':
                    n2 = n2 * 10 + int(ligne[indice + taille])
                    taille += 1

                if (ligne[indice + taille] == ")" and n2 < 1000):
                    somme += n1 * n2
        elif ligne[indice:indice+4] == "do()":
            testCumul = True
        elif ligne[indice:indice+7] == "don't()":
            testCumul = False

print(somme)