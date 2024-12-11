def estValide(res, val, op, total):
    if len(val) > 0:
        if op == "first":
            return estValide(res, val[1:], "produit", val[0]) or estValide(res, val[1:], "somme", val[0])
        elif op == "produit":
            return estValide(res, val[1:], "produit", total*val[0]) or estValide(res, val[1:], "somme", total*val[0])
        elif op == "somme":
            return estValide(res, val[1:], "produit", total+val[0]) or estValide(res, val[1:], "somme", total+val[0])
    else:
        return total == res

f = open("input.txt", "r")

somme = 0

for x in f:
    ligne = x[:-1].split(":")
    res = int(ligne[0])
    val = [int(ele) for ele in ligne[1][1:].split(" ")]
    if estValide(res,val,"first", 0):
        somme += res

print(somme)