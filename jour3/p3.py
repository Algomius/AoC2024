f = open("input.txt", "r")

somme = 0

for l in f:
    indice = l.find("mul(")
    while  indice != -1:
        indice += 4
        n1 = 0
        i= 0
        while l[indice + i] >= '0' and l[indice + i] <= '9':
            n1 = n1 * 10 + int(l[indice + i])
            i += 1
        
        if (l[indice + i] == "," and n1 < 1000):
            i += 1
            n2 = 0
            while l[indice + i] >= '0' and l[indice + i] <= '9':
                n2 = n2 * 10 + int(l[indice + i])
                i += 1

            if (l[indice + i] == ")" and n2 < 1000):
                somme += n1 * n2 
        l = l[indice+i:]
        indice = l.find("mul(")
    
print(somme)