f = open("input.txt", "r")


testSpace = False
word = []
indice = 0
for x in f:
    l =  [int(e) for e in list(x[:-1])]
    for e in l:
        cpt = e
        while cpt > 0:
            if testSpace:
                word.append(None)
            else:
                word.append(indice)
            cpt -= 1
        if testSpace:
            indice += 1 
        testSpace = not testSpace

deb = 0
fin = len(word)-1

while deb < fin:
    while word[deb] != None and deb < fin:
        deb += 1

    while word[fin] == None and deb < fin:
        fin -= 1

    if deb < fin:
        word[deb], word[fin] = word[fin], word[deb]


somme = 0
indice = 0
while word[indice] != None:
    somme += word[indice] * indice
    indice += 1

print(somme)
