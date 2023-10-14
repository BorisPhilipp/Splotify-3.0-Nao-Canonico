import time

class Menu:
    def __init__(self, opcao=0):
        self._opcao = opcao

    @property
    def mensagens(self):
        tupla_mensagens = ("""
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
                    * JEB Productions *""", """
              
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

they're taking the hobbits to isengard.              

              """)

        return tupla_mensagens

    def exibir_menu_principal(self):
        mensagem_escolha = ["\n╔════════════════════════╗", "           MENU ", " * [1] - Music", " * [2] - Lista de Músicas", " * [3] - Fechar", "╚════════════════════════╝\n"]

        print(self.mensagens[0])
        time.sleep(1)
        for i in range(len(mensagem_escolha)):
            print(mensagem_escolha[i])
