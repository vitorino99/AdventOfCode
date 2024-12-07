from utils import ler_arquivo_txt


coluna1, coluna2 = ler_arquivo_txt('day1/input.txt')
coluna1.sort(),coluna2.sort()


resultado = 0
tamanho_lista1 = len(coluna1)
tamanho_lista2 = len(coluna2)

for x in range(0,tamanho_lista1):
    resultado += abs(coluna1[x] - coluna2[x])

print(resultado)