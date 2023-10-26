class Artes:
    def printarLogoPrograma():
        print("""
/$$$$$$            /$$             /$$     /$$  /$$$$$$          
/$$__  $$          | $$            | $$    |__/ /$$__  $$         
| $$  \__/  /$$$$$$ | $$  /$$$$$$  /$$$$$$   /$$| $$  \__//$$   /$$
|  $$$$$$  /$$__  $$| $$ /$$__  $$|_  $$_/  | $$| $$$$   | $$  | $$
\____  $$| $$  \ $$| $$| $$  \ $$  | $$    | $$| $$_/   | $$  | $$
/$$  \ $$| $$  | $$| $$| $$  | $$  | $$ /$$| $$| $$     | $$  | $$
|  $$$$$$/| $$$$$$$/| $$|  $$$$$$/  |  $$$$/| $$| $$     |  $$$$$$$
\______/ | $$____/ |__/ \______/    \___/  |__/|__/      \____  $$
        | $$                                            /$$  | $$
        | $$                                           |  $$$$$$/ 
        |__/                                            \______/ 
                    * JEB Productions *""")

    def printarArteBye():
        print("""
              
 ▄▄▄▄ ▓██   ██▓▓█████ 
▓█████▄▒██  ██▒▓█   ▀ 
▒██▒ ▄██▒██ ██░▒███   
▒██░█▀  ░ ▐██▓░▒▓█  ▄ 
░▓█  ▀█▓░ ██▒▓░░▒████▒
░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░
▒░▒   ░▓██ ░▒░  ░ ░  ░
 ░    ░▒ ▒ ░░     ░   
 ░     ░ ░        ░  ░
      ░░ ░            
              """)

import Musica
class Menus():
    def printarMenuEscolhaPrincipal():
        print("\n╔════════════════════════╗\n           MENU \n * [1] - Music\n * [2] - Lista de Músicas\n * [3] - Fechar\n╚════════════════════════╝\n")

    def printarPlaylists(arquivo_musicas):
        musica = Musica.Playlist(arquivo_musicas)
        musica.separar_arquivo_em_lista()
        for i in musica._playlists_compactadas:
            print(i, '\n')
    

import Funcionalidades
class MenuPrincipal:  
    def setup(self):
        Artes.printarLogoPrograma()
        Funcionalidades.timer(2)
        Funcionalidades.apagarTela
        Menus.printarMenuEscolhaPrincipal()
        Funcionalidades.OptionMenuUsuario.verificadorOptionMenuPrincipal()