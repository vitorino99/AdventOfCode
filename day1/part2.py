from utils import ler_arquivo_txt


coluna1,coluna2 = ler_arquivo_txt('day1/input.txt')
resultado = 0
map = {}

for valor in coluna2:
    if valor in coluna1:
        map[valor] = map.get(valor,0) + 1
        
for x,y in map.items(): 
    resultado += x * y
    

print(resultado)