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


class PlaylistSetup(Playlist):
    def __init__(self, arquivo_com_musicas):
        super().__init__(arquivo_com_musicas)
        self.separar_arquivo_em_lista()

    def verificadorOptionPlaylist(self):
        while True:
            user_input = int(input("Digite o número da playlist: "))
            
            if 0 <= user_input <= len(self._playlists_compactadas):
                self._playlist = self._playlists_compactadas[user_input]
                SelecionarMusica(self._playlist).iniciar()
                break
                    
            else:
                print("Playlist inválida!")
                

import pygame
class SelecionarMusica:
    def __init__(self, playlist):
        self._playlist = playlist
        pygame.mixer.init()
        
    def iniciar(self):
        pygame.mixer.music.load(f"music/{self._playlist[0]}")
        pygame.mixer.music.play()
        while pygame.mixer.get_busy:
            pass