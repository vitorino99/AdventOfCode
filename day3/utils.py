def ler_arquivo_txt(caminho):
    with open(caminho, 'r') as file:
        return file.read()
    