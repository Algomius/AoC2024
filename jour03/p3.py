fic = open("input.txt", "r")

somme = 0

for ligne in fic:
    indice = ligne.find("mul(")
    while indice != -1:
        indice = indice + 4
        n1 = 0
        taille = 0
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
        ligne = ligne[indice + taille:]
        indice = ligne.find("mul(")
print(somme)