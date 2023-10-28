import os, time, threading, random

class MusicPlayer:
    def __init__(self, arquivo_de_musicas):
        self._arquivo = arquivo_de_musicas
        self._indice_musica_atual = 0
        self._playlist_atual = None

        organizador = OrganizadorPlaylist(self._arquivo)
        organizador.ler_arquivo()
        self._playlist = organizador._playlists_compactadas
        self._tocador = Tocador()
    
    def printar_playlist(self):
        self.limpar_tela()
        for i in range(len(self._playlist)):
            print(f" * Playlist [{i}]: {self._playlist[i]} \n")

    def selecionar_playlist(self):
        self.printar_playlist()
        user_input_p = int(input("Selecione o número da playlist: "))
        self._playlist_atual = self._playlist[user_input_p]
        self._tocador.tocar_musica(self._playlist_atual, self._indice_musica_atual)
        self._verificador_mudo = False
        return

    def limpar_tela(self):
        os.system('clear' if os.name == 'posix' else 'CLS')

    def timer(self, segundos):
        time.sleep(segundos)

    def lancar_menu_inicial(self):
        def verificador_musica():
            while True:
                if not pygame.mixer.music.get_busy() and self._verificador_mudo == False:
                    if self._indice_musica_atual < len(self._playlist_atual) - 1:
                        self._indice_musica_atual += 1
                    else:
                        self._indice_musica_atual = 0
                    self._tocador.tocar_musica(self._playlist_atual, self._indice_musica_atual)
                self.timer(1)


        print("""
    /$$$$$$            /$$             /$$     /$$  /$$$$$$          
    /$$__  $$          | $$            | $$    |__/ /$$__  $$         
    | $$  \__/  /$$$$$$ | $$  /$$$$$$  /$$$$$$   /$$| $$  \__//$$   /$$
    | $$$$$$  /$$__  $$| $$ /$$__  $$|_  $$_/  | $$| $$$$   | $$  | $$
    \____  $$| $$  \ $$| $$| $$  \ $$  | $$    | $$| $$_/   | $$  | $$
    /$$  \ $$| $$  | $$| $$| $$  | $$  | $$ /$$| $$| $$     | $$  | $$
    | $$$$$$/| $$$$$$$/| $$|  $$$$$$/  |  $$$$/| $$| $$     |  $$$$$$$
    \______/ | $$____/ |__/ \______/    \___/  |__/|__/      \____  $$
            | $$                                            /$$  | $$
            | $$                                           |  $$$$$$/ 
            |__/                                            \______/ 
                        * JEB Productions *""")
        self.timer(2)
        
        while True:
            self.limpar_tela()
            print("\n╔════════════════════════╗", "\n           MENU ", "\n * [1] - Music", "\n * [2] - Lista de Músicas", "\n * [3] - Fechar", "\n╚════════════════════════╝\n")
            user_input = int(input("Escolha uma opção: "))

            if user_input == 1:
                self.selecionar_playlist()
                background_thread = threading.Thread(target=verificador_musica)
                background_thread.daemon = True
                background_thread.start()

                while True:
                    self.limpar_tela()
                    print(f"""Current Playing: {self._tocador._musica_atual}\n\nFunções disponiveis:\n* [1] Play{" "*13}* [2] Pause\n* [3] Replay {" "*10}* [4] Loop\n* [5] Próxima{" "*10}* [6] Retornar\n* [7] Aleatório{" "*8}* [8] Escolher Outra Playlist\n* [9] Ver a próxima música\n\n* [0] Sair""")
                    user_input = int(input("\nDigite uma das opções: "))

                    if user_input == 0:
                        self._verificador_mudo = True
                        pygame.mixer.music.stop()
                        break

                    elif user_input == 1:
                        self._verificador_mudo = False
                        pygame.mixer.music.unpause()

                    elif user_input == 2:
                        self._verificador_mudo = True
                        pygame.mixer.music.pause()

                    elif user_input == 3:
                        self._verificador_mudo = False
                        pygame.mixer.music.play()

                    elif user_input == 4:
                        self._verificador_mudo = False
                        pygame.mixer.music.play(-1)

                    elif user_input == 5:
                        self._verificador_mudo = False
                        if self._indice_musica_atual < len(self._playlist_atual) - 1:
                            self._indice_musica_atual += 1
                            self._tocador.tocar_musica(self._playlist_atual, self._indice_musica_atual)
                        else:
                            self._indice_musica_atual = 0
                            self._tocador.tocar_musica(self._playlist_atual, self._indice_musica_atual)

                    elif user_input == 6:
                        self._verificador_mudo = False
                        if self._indice_musica_atual > 0:
                            self._indice_musica_atual -= 1
                        else:
                            self._indice_musica_atual = len(self._playlist_atual) - 1
                        self._tocador.tocar_musica(self._playlist_atual, self._indice_musica_atual)
                        
                    elif user_input == 7:
                        self._verificador_mudo = False
                        if len(self._playlist_atual) > 1:
                            while True:
                                numero =  random.randint(0, len(self._playlist_atual) - 1)
                                if numero != self._indice_musica_atual:
                                    self._indice_musica_atual = numero
                                    break
                        self._tocador.tocar_musica(self._playlist_atual, self._indice_musica_atual)

                    elif user_input == 8:
                        self._verificador_mudo = True
                        pygame.mixer.music.stop()
                        self._indice_musica_atual = 0
                        
                        self.selecionar_playlist()
                        
                    elif user_input == 9:
                        self._verificador_mudo = False
                        print(f"A próxima música da playlist será: {self._playlist_atual[self._indice_musica_atual+1 if len(self._playlist_atual) > 1 else self._indice_musica_atual]}")
                        self.timer(2)

                    else:
                        print("Inválido!")
                        self.timer(1)
                        
            elif user_input == 2:
                self.printar_playlist()
                input()

            elif user_input == 3:
                exit()

            else:
                print("Inválido!")
                self.timer(1)


class OrganizadorPlaylist:
    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo

    def ler_arquivo(self):
        with open(self._nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas_brutas = arquivo.readlines()
            linhas = [x.replace("\n", "") for x in linhas_brutas]
        self._playlists_compactadas = [linhas[x:x+3] for x in range(0, len(linhas), 3)]


import pygame
class Tocador:
    def __init__(self) -> None:
        self._musica_atual = None

    def tocar_musica(self, lista, indice):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(f"music/{lista[indice]}")
        self._musica_atual = lista[indice]
        pygame.mixer.music.play()