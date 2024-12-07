from utils import ler_arquivo_txt


coluna1, coluna2 = ler_arquivo_txt('day1/input.txt')
coluna1.sort(),coluna2.sort()
resultado = 0

for x in range(0,len(coluna1)):
    resultado += abs(coluna1[x] - coluna2[x])

print(resultado)