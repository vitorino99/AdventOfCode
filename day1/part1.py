coluna1 = []
coluna2 = []


with open("AdventOfCode/day1/input.txt", 'r') as file:
    for line in file:
        valores = line.split()
        if len(valores) == 2:
            coluna2.append(int(valores[0]))
            coluna1.append(int(valores[1]))
    coluna1.sort()
    coluna2.sort()

resultado = 0
tamanho_lista1 = len(coluna1)
tamanho_lista2 = len(coluna2)

for x in range(0,tamanho_lista1):
    resultado += abs(coluna1[x] - coluna2[x])

print(resultado)