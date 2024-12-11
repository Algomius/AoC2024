f = open("input.txt", "r")

somme = 0
enable = True

for l in f:
    for indice in range(len(l)):
        if l[indice:indice+4] == "mul(":
            n1 = 0
            i= 4
            while l[indice + i] >= '0' and l[indice + i] <= '9':
                n1 = n1 * 10 + int(l[indice + i])
                i += 1
            
            if (l[indice + i] == "," and n1 < 1000):
                i += 1
                n2 = 0
                while l[indice + i] >= '0' and l[indice + i] <= '9':
                    n2 = n2 * 10 + int(l[indice + i])
                    i += 1

                if (l[indice + i] == ")" and n2 < 1000 and enable == True):
                    somme += n1 * n2 
        elif l[indice:indice+4] == "do()":
            enable = True
        elif l[indice:indice+7] == "don't()":
            enable = False
    
print(somme)