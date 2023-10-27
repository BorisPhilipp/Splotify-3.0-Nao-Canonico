class Playlist:
    def __init__(self, arquivo_playlist):
        self._arquivo = arquivo_playlist
        self._playlists_compactadas = []
        self._playlist = []

    @property
    def arquivo(self):
        return self._arquivo
    
    @arquivo.setter
    def arquivo(self, nome_do_arquivo):
        self._arquivo = nome_do_arquivo

    def separar_arquivo_em_lista(self):
        with open(self._arquivo, 'r', encoding='utf-8') as arquivo:
            linhas_brutas = arquivo.readlines()
            linhas = [x.replace("\n", "") for x in linhas_brutas]

        self._playlists_compactadas = [linhas[x:x+3] for x in range(0, len(linhas), 3)]               # List Comprehension aplicada na separação das músicas em chunks

