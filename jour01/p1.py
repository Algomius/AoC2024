f = open("input.txt", "r")

first = []
last = []
for x in f:
    l = x[:-1].split(" ")
    first.append(int(l[0]))
    last.append(int(l[3]))
first.sort()
last.sort()

somme = 0

for i in range(len(first)):
    somme += abs(first[i]-last[i])

print(somme)