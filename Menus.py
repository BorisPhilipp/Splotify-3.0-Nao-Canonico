import time
from Lista import Lista

class Menu:
    def __init__(self):
        self._opcao = int


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
    

    @property
    def opcao(self):
        return self._opcao


    @opcao.setter
    def opcao(self, valor):
        if valor in [1,2,3,4,5,6,7,8,9,0]:
            self._opcao = valor
        else:
            print("Valor inválido.")


    def exibir_menu_principal(self):
        mensagem_escolha = ["\n╔════════════════════════╗", "           MENU ", " * [1] - Music", " * [2] - Lista de Músicas", " * [3] - Fechar", "╚════════════════════════╝\n"]

        print(self.mensagens[0])
        time.sleep(1)
        for i in range(len(mensagem_escolha)):
            print(mensagem_escolha[i])

    def exibir_fim(self):
        time.sleep(1)
        print(self.mensagens[1])