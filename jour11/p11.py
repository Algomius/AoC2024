f = open("input.txt", "r")


for x in f:
    ancien = ([int(e) for e in x[:-1].split(" ")])
    for _ in range(25):
        actuel = []
        for e in ancien:
            if e == 0:
                actuel.append(1)
            elif len(str(e)) % 2 == 0:
                strE = str(e)
                actuel.append(int(strE[:len(strE)//2]))
                actuel.append(int(strE[len(strE)//2:]))
            else:
                actuel.append(e * 2024)

        ancien = actuel[:]
    print(len(ancien))

