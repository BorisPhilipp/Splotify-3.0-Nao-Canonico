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
        for i in range(len(musica._playlists_compactadas)):
            print(f" - Playlist [{i}]: {musica._playlists_compactadas[i]}\n")
    

import Funcionalidades
class MenuPrincipal:  
    def setup(nome_do_arquivo_com_musicas):
        Artes.printarLogoPrograma()
        Funcionalidades.timer(2)
        Funcionalidades.apagarTela
        Menus.printarMenuEscolhaPrincipal()
        Funcionalidades.OptionMenuUsuario.verificadorOptionMenuPrincipal()