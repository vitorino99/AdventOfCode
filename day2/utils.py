#Poderia fazer aplicando a validação diretamente nessa leitura
#Mas quis deixar assim para manter o formato de leitura do TXT
#Isso acontece pois não consegui ler o arquivo txt diretamente como int

def ler_arquivo_txt(caminho):
    resultado = []
    with open(caminho, 'r') as file:
        for line in file:
            valores = line.split()
            lista = []
            for num in valores:
                lista.append(int(num))      
            resultado.append(lista)
    
    return resultado