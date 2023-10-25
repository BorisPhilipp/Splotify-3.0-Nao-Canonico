class Playlist:
    def __init__(self, arquivo_playlist):
        self._arquivo = arquivo_playlist
        self._playlist = []


    @property
    def arquivo(self):
        return self._arquivo
    
    @arquivo.setter
    def arquivo(self, nome_do_arquivo):
        self._arquivo = nome_do_arquivo

    def separar_arquivo_em_lista(self):
        with open(self.arquivo) as arquivo:
            linhas = arquivo.readlines()

        for indice, linha in enumerate(linhas):
            if indice % 3 == 0:
                break
            self._playlist.append(linha)