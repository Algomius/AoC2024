f = open("input.txt", "r")

somme = 0

for x in f:
    l = x[:-1].split(" ")
    sens = "None"
    last = int(l[0])
    test = True
    for e in [int(ele) for ele in l[1:]]:
        if sens == "None":
            if e > last and abs(e - last) <= 3:
                sens = "Croissant"
            elif e < last and abs(e - last) <= 3:
                sens = "Decroissant"
            else:
                test = False
        elif sens == "Decroissant":
            if e >= last:
                test = False
            elif abs(e - last) > 3:
                test = False
        elif sens == "Croissant":
            if e <= last:
                test = False
            elif abs(e - last) > 3:
                test = False
        last = e

    if test:
        print(x, end="")
        somme += 1  
    

print(somme)