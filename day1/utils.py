def ler_arquivo_txt(caminho):
    lista1 = []
    lista2 = [] 
    with open(caminho, 'r') as file:
        for line in file:
            valores = line.split()
            if len(valores) == 2:
                lista1.append(int(valores[0]))
                lista2.append(int(valores[1]))
    
    return lista1,lista2