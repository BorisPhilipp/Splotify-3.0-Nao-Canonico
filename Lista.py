class Fabricador:
    def __init__(self, playlist):
        self._playlist = playlist
    
    @property
    def arquivo(self):
        return self._playlist
    
    @arquivo.setter
    def arquivo(self, novo_arquivo):
        if novo_arquivo != "":
            self._playlist = novo_arquivo

    @property
    def lista_musicas(self):
        with open(self.arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        bloco_atual = []
        blocos = []

        for i, linha in enumerate(linhas):
            bloco_atual.append(linha.split())
            if (i + 1) % 3 == 0:
                blocos.append(bloco_atual)
                bloco_atual = []
        
        if bloco_atual:
            blocos.append(bloco_atual)
        
        return blocos


'''@property
    def lista_musicas(self):
        with open(self._playlist, 'r') as arquivoMusicas:
            quantidade = len(arquivoMusicas.readlines())
        
        with open(self._playlist, 'r') as arquivoMusicas:
            arquivoMusicas.seek(0)
            
            contador = 1
            for i in range(int(quantidade/3)):
                blocoMusicas = []
                for j in range(3):
                    texto = arquivoMusicas.readline().strip()
                    blocoMusicas.append(texto)
                self._listaMusica.append(blocoMusicas)

        return self._listaMusica'''


class Lista(Fabricador):
    def __init__(self, playlist):
        super().__init__(playlist)

    def listar_musicas(self):
        for i, musicas in enumerate(self.lista_musicas):
            print(f"* Playlist {i+1}: ", end="")
            
            for indice, musica in enumerate(musicas):
                print(musica, end="")
                if indice < len(musicas) - 1:
                    print(', ', end="")

            if i != len(self.lista_musicas)-1:
                print('\n')
            else:
                print()
