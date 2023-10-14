class Playlist:
    def __init__(self, lista):
        self._lista = lista
        self._playlist = []
        self._musica = ''

    @property
    def playlist(self):  
        return self._playlist

    @playlist.setter
    def playlist(self, indice):
        self._playlist = self._lista[indice]

    def selecaoPlaylist(self, indice_input):
        self.playlist = indice_input
        self._musica = ''.join(self.playlist[0])            # Configura a musica atual para a musica indice[0]


class Player(Playlist):
    def __init__(self, lista):
        super().__init__(lista)
    
    def tocarMusica(self):
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(f'music/{self._musica}')
        print('Tocando musica 1: ')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass