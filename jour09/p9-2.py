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

fin = len(word)-1

while 0 < fin:
    while word[fin] == None and 0 < fin:
        fin -= 1

    if 0<fin :
        num = word[fin]
        nbNum = 0
        while word[fin] == num:
            fin -=1
            nbNum += 1

        fin += 1

        enoughSpace = False
        deb = 0
        while not enoughSpace and deb <fin:

            while word[deb] != None and deb < fin:
                deb += 1

            nbNone = 1
            while word[deb+ nbNone] == None and deb+nbNone < len(word):
                nbNone += 1


            if nbNone >= nbNum:
                enoughSpace = True
                for ind in range(nbNum):
                    word[deb+ind], word[fin+ind] = word[fin+ind], word[deb+ind]
                fin -= 1
            else:
                deb += nbNone +1 

        if not enoughSpace:
            fin -= 1

somme = 0
indice = 0
for e in word:
    if e != None:
        somme += e * indice
    indice += 1

print(somme)
