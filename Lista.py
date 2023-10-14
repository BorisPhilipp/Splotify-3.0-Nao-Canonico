class Lista:
    def __init__(self):
        self._musicas = ['1', '\n', '2', '\n', '3', '\n']
    
    def escreve(self):
        arquivo = open("teste.txt", 'w', encoding='utf-8')
        arquivo.writelines(self._musicas)
