from Lista import Lista
from Musica import Player
import time, os

class Menus:
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
        if valor in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
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
        
    def exibir_player_opcoes(self, musica):
        print(f"""Current Playing: {musica}\n\nFunções disponiveis:\n* [1] Play{" "*13}* [2] Pause\n* [3] Replay {" "*10}* [4] Loop\n* [5] Próxima{" "*10}* [6] Retornar\n* [7] Aleatório{" "*8}* [8] Escolher Outra Playlist\n* [9] Ver a última música\n\n* [0] Sair""")


class MenuPrincipal(Menus):
    def __init__(self, arquivo_com_nomes_de_musicas):
        super().__init__()                                     
        self._lista = Lista(arquivo_com_nomes_de_musicas)           # Cria um objeto Lista passando o arquivo de músicas
        self._player = Player(self._lista.lista_musicas)            # Cria um objeto Player passando uma LISTA do arquivo com músicas lido

    def selecao_menu_principal(self):
        os.system('clear' if os.name == 'posix' else 'CLS')
        self.exibir_menu_principal()

        while True:
            self.opcao = int(input("Digite uma opção: "))
            opcao = self.opcao
            if opcao in (1,2,3):
                break
            print("Opcao invalida")

        if opcao == 1:
            print()
            self._lista.listar_musicas()
            self._player.selecaoPlaylist(int(input("\nDigite o numero correspondente a playlist: ")) - 1)
            self._player.tocarMusica()
            
            self.exibir_player_opcoes(self._player._musica)
            
            while True:
                user_input = (int(input("\nDigite a opção: ")))
                if user_input in (0,1,2,3,4,5,6,7,8,9):
                    if user_input == 5:
                        self._player.mudar_proxima_musica()
                    else:
                        print("Função ainda não disponível, funções disponíveis (Próxima)")
                else:
                    print("Número inválido!")

        elif opcao == 2:
            print()
            self._lista.listar_musicas()
            input("\nPressione qualquer tecla para sair...")
            self.selecao_menu_principal()

        elif opcao == 3:
            self.exibir_fim()
            exit()


def iniciar_programa(arquivo_com_musicas):
    menuprincipal = MenuPrincipal(arquivo_com_musicas)
    menuprincipal.selecao_menu_principal()