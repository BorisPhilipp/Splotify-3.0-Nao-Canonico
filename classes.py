from leitura_escrita import Leitura, Escrita
from Tocador import Tocador

class MusicPlayer:
    def __init__(self, arquivo_de_musicas, playlist_atual=None):
        self._tocador = None
        self._arquivo = arquivo_de_musicas
        self._playlist_atual = playlist_atual
        self._playlists = OrganizadorPlaylist(self._arquivo).ler_arquivo()
    
    def printar_playlist(self):
        Tocador().limpar_tela()
        for i in range(len(self._playlists)):
            print(f" * Playlist [{i}]: {self._playlists[i]} \n")

    def selecionar_playlist(self):
        self.printar_playlist()
        while True:
            user_input_p = int(input("Selecione o número da playlist: "))
            if 0 <= user_input_p < len(self._playlists):
                break
            else:
                print("Playlist errada!")

        self._playlist_atual = self._playlists[user_input_p]
        self._tocador = Tocador(self._playlists, self._playlist_atual)
        self._tocador.tocar_musica()

    def lancar_menu_inicial(self):
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
        Tocador().timer(1)
        
        while True:
            Tocador().limpar_tela()
            print("\n╔════════════════════════╗", "\n           MENU ", "\n * [1] - Music", "\n * [2] - Lista de Músicas", "\n * [3] - Fechar", "\n╚════════════════════════╝\n")
            user_input = int(input("Escolha uma opção: "))

            if user_input == 1:
                self.selecionar_playlist()
                self._tocador.funcoes()

            elif user_input == 2:
                self.printar_playlist()
                input()

            elif user_input == 3:
                exit()

            else:
                print("Inválido!")
                Tocador().timer(1)


class OrganizadorPlaylist:
    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo

    def ler_arquivo(self):
        with open(self._nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas_brutas = arquivo.readlines()
            linhas = [x.replace("\n", "") for x in linhas_brutas]
        self._playlists_compactadas = [linhas[x:x+3] for x in range(0, len(linhas), 3)]
        return self._playlists_compactadas