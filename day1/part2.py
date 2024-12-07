from utils import ler_arquivo_txt


coluna1,coluna2 = ler_arquivo_txt('day1/input.txt')
resultado = 0
map = {}

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