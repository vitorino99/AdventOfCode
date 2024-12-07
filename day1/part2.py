coluna1  = []
coluna2 = []
resultado = 0
map = {}

with open("AdventOfCode/day1/input.txt", 'r') as file:
    for line in file:
        valores = line.split()
        if len(valores) == 2:
            coluna1.append(int(valores[0]))
            coluna2.append(int(valores[1]))

for valor in coluna2:
    if valor in coluna1:
        if valor not in map.keys():
            map[valor] = 1
        else:
            map[valor] += 1

for x in coluna1:   
    if x in map.keys():
        resultado += x * map[x]
    

print(resultado)