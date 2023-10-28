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


class Menus():
    def printarMenuEscolhaPrincipal():
        print("\n╔════════════════════════╗\n           MENU \n * [1] - Music\n * [2] - Lista de Músicas\n * [3] - Fechar\n╚════════════════════════╝\n")


import time, Funcionalidades
class MenuPrincipal:  
    def setup(self):
        Artes.printarLogoPrograma()
        time.sleep(2)
        apagarTela()
        Menus.printarMenuEscolhaPrincipal()
        Funcionalidades.OptionMenuUsuario.verificadorOptionMenuPrincipal()


import os
def apagarTela():
    os.system('clear' if os.name == 'posix' else 'CLS')