coluna1 = []
coluna2 = []


with open("AdventOfCode/day1/input.txt", 'r') as file:
    for line in file:
        valores = line.split()
        if len(valores) == 2:
            coluna2.append(int(valores[0]))  
            coluna1.append(int(valores[1]))  
            
resultado = 0
tamanho_lista1 = len(coluna1)
tamanho_lista2 = len(coluna2)

for x in range(0,tamanho_lista1):
    menor_valor_lista_1 = min(coluna1)
    menor_valor_lista_2 = min(coluna2)
    resultado += abs(menor_valor_lista_1 - menor_valor_lista_2)
    coluna1.remove(menor_valor_lista_1)
    coluna2.remove(menor_valor_lista_2)

print(resultado)
    
    