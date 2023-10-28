import Musica, pygame

class SelecionarMusica:
    def __init__(self, playlist):
        self._playlist = playlist
        pygame.mixer.init()
        
    def iniciar(self):
        pygame.mixer.music.load(f"music/{self._playlist[0]}")
        pygame.mixer.music.play()


class Opcoes(Musica.PlaylistSetup):
    def __init__(self):
        super().__init__()
        self._indice_musica_atual = 0

    def proxima_musica(self):
        if self._indice_musica_atual < 3:
            self._indice_musica_atual += 1
        else:
            self._indice_musica_atual = 0

        pygame.mixer.music.load(f"music/{self._playlist[self._indice_musica_atual]}")

    def tocar(self):
        pygame.mixer.music.play()
        while pygame.mixer.get_busy:
            pass
    