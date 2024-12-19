from utils import ler_arquivo_txt

valores = ler_arquivo_txt('day2/input.txt')
result = 0
def verificar_valores_valido(linha: list) -> int: 
    lista_ordenada = sorted(linha)
    
    if linha != lista_ordenada and linha != lista_ordenada[::-1]:
        return 0

    for x in range(1, len(linha)):
        dif  = abs((linha[x]) - (linha[x-1]))
        if dif < 1 or dif > 3:
            return 0
    return 1
        
for x in valores:
    result += verificar_valores_valido(x)

print(result)