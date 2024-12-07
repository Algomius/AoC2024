f = open("input.txt", "r")

somme = 0

for x in f:
    l = x[:-1].split(" ")
    sens = "None"
    last = int(l[0])
    error = 0
    for e in [int(ele) for ele in l[1:]]:
        if sens == "None":
            if e > last and abs(e - last) <= 3:
                sens = "Croissant"
            elif e < last and abs(e - last) <= 3:
                sens = "Decroissant"
            else:
                error += 1
        elif sens == "Decroissant":
            if e >= last:
                error += 1
            elif abs(e - last) > 3:
                error += 1
        elif sens == "Croissant":
            if e <= last:
                error += 1
            elif abs(e - last) > 3:
                error += 1
        last = e

    if error < 2:
        somme += 1  
    

print(somme)