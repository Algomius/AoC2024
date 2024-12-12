dict = {}

def nbPierres(n, coups):
    if coups == 0:
        return 1
    elif (n,coups) in dict:
        return dict[(n, coups)]
    else:
        somme = 0
        if n == 0:
            somme = nbPierres(1, coups-1)
        elif len(str(n)) % 2 == 0:
            strN = str(n)
            somme += nbPierres(int(strN[:len(strN)//2]),coups-1)
            somme += nbPierres(int(strN[len(strN)//2:]),coups-1)
        else:
            somme += nbPierres(n * 2024, coups-1)
        dict[(n, coups)] = somme
        return somme

f = open("input.txt", "r")

somme = 0
for x in f:
    ancien = ([int(e) for e in x[:-1].split(" ")])
    for e in ancien:
        somme += nbPierres(e, 75)
    print(somme)

