import os, pygame

class Playlist:
    def __init__(self, lista):
        self._lista = lista
        self._playlist = []
        self._musica = ''
        self._indice = 0

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
        pygame.mixer.init()
    
    def tocarMusica(self):
        pygame.mixer.music.load(f'music/{self._musica}')
        pygame.mixer.music.play()
            
    def mudar_proxima_musica(self):
        for sublista in self.playlist:
            if self._musica in sublista:
                indice = self.playlist.index(sublista)
                break
        if indice < len(self.playlist) - 1:
            indice += 1
            self._musica = ''.join(self.playlist[indice])
        else:
            indice = 0
            self._musica = ''.join(self.playlist[indice])
        self.tocarMusica()
        