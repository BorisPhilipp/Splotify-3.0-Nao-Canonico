import random, pygame, os, time

class MusicPlayer:
    mensagem_introducao = ("""
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

    def __init__(self):
        os.chdir('./music')
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)

        self.playlist1 = []
        self.playlist2 = []

        self.create_playlists()

        self.indice = 0
        self.musica_atual = ""
        self.playlist_selecionada = []

    def create_playlists(self):
        self.musicas = []
        self.enqueue(self.musicas, 'kill_again.mp3')
        self.enqueue(self.musicas, 'eazy_duz_it.mp3')
        self.enqueue(self.musicas, 'check_yo_self.mp3')
        self.enqueue(self.musicas, 'chamber_of_reflection.mp3')
        self.enqueue(self.musicas, '2_much.mp3')
        self.enqueue(self.musicas, 'hey_ya.mp3')

        for i in range(3):
            musica = self.dequeue(self.musicas)
            self.playlist1.append(musica)

        for i in range(3):
            musica = self.dequeue(self.musicas)
            self.playlist2.append(musica)

    def is_empty(self, pilha):
        return len(pilha) == 0

    def pop(self, pilha):
        if not self.is_empty(pilha):
            return pilha.pop()
        else:
            return "A pilha está Vazia."

    def push(self, pilha, elemento):
        return pilha.append(elemento)

    def enqueue(self, fila, elemento):
        return fila.append(elemento)

    def dequeue(self, fila):
        if len(fila) == 0:
            return "A fila está vazia."
        else:
            return fila.pop(0)

    def limparTela(self):
        _ = os.system('clear' if os.name == 'posix' else 'cls')

    def timer(self, x):
        time.sleep(x)

    def ListaMusicas(self):
        self.limparTela()
        print("┌──────────────────────────────┐\n", " " * 7, "- ̗̀  MÚSICAS ̖́  -", "\n└──────────────────────────────┘")
        print("\n-> PLAYLIST1:", end=" ")

        for i in range(len(self.playlist_selecionada)):
            print(self.playlist_selecionada[i].replace(".mp3", " / "), end="")
        print()

        input("\n\nPressione ENTER para sair da tela...")
        self.StartMenu()

    def StartMenu(self):
        opcoes_menu = []
        self.push(opcoes_menu, "╚════════════════════════╝\n")
        self.push(opcoes_menu, " * [3] - Fechar")
        self.push(opcoes_menu, " * [2] - Lista de Músicas")
        self.push(opcoes_menu, " * [1] - Music")
        self.push(opcoes_menu, "           MENU ")
        self.push(opcoes_menu, "\n╔════════════════════════╗")
        self.limparTela()
        print(self.mensagem_introducao[0])
        self.timer(1)
        for i in range(len(opcoes_menu)):
            print(self.pop(opcoes_menu))

        self.menuOpcoes()

    def menuOpcoes(self):
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            self.menuSelecaoPlaylist()
        elif escolha == "2":
            self.ListaMusicas()
        elif escolha == "3":
            print(self.mensagem_introducao[1])
            exit()
        else:
            print("Opção inválida. Escolha novamente.")
            self.timer(1.5)
            self.limparTela()
            self.StartMenu()

    def menuSelecaoPlaylist(self):
        self.limparTela()
        print(" Playlists Encontradas no Sistema: \n* [1] Playlist1\n* [2] Playlist2")
        user_selection = int(input("Digite o número da playlist: "))
        if user_selection == 1:
            self.playlist_selecionada = self.playlist1
        elif user_selection == 2:
            self.playlist_selecionada = self.playlist2
        else:
            self.limparTela()
            print("""
┳┓┳┳┳┳┓┏┓┳┓┏┓  ┏┓┳┓┳┓┏┓┳┓┏┓
┃┃┃┃┃┃┃┣ ┣┫┃┃  ┣ ┣┫┣┫┣┫┃┃┃┃
┛┗┗┛┛ ┗┗┛┛┗┗┛  ┗┛┛┗┛┗┛┗┻┛┗┛                      
""")
            self.timer(1.5)
            self.menuSelecaoPlaylist()
        for i in range(10):
            self.limparTela()
            print(f"A próxima música será: {self.playlist_selecionada[self.indice]}")
            self.timer(0.2)
        self.selecaoDeMusica("proxima")

    def selecaoDeMusica(self, tipo):
        if tipo == "proxima":
            if self.indice != len(self.playlist_selecionada) - 1:
                self.indice += 1
            else:
                self.indice = 0
        elif tipo == "anterior":
            if self.indice != 0:
                self.indice -= 1
            else:
                self.indice = len(self.playlist_selecionada) - 1
        elif tipo == "random":
            self.indice = random.randint(0, len(self.playlist_selecionada) - 1)
        self.musica_atual = self.playlist_selecionada[self.indice]
        self.tocarMusica(self.musica_atual)

    def tocarMusica(self, musica):
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play()
        self.playerMusicaMenu()

    def playerMusicaMenu(self):
        verificador = 0
        while verificador != 1:
            self.limparTela()
            print(f"""Current Playing: {self.musica_atual}\n\nFunções disponíveis:\n* [1] Play{" " * 13}* [2] Pause\n* [3] Replay {" " * 10}* [4] Loop\n* [5] Próxima{" " * 10}* [6] Retornar\n* [7] Aleatório{" " * 8}* [8] Escolher Outra Playlist\n* [9] Ver a última música\n\n* [0] Sair""")
            term = int(input("Digite o número da opção: "))
            match term:
                case 0:
                    pygame.mixer.music.stop()
                    self.limparTela()
                    verificador = 1
                    break
                case 1:
                    pygame.mixer.music.unpause()
                case 2:
                    pygame.mixer.music.pause()
                case 3:
                    pygame.mixer.music.play()
                case 4:
                    pygame.mixer.music.play(-1)
                case 5:
                    self.selecaoDeMusica("proxima")
                case 6:
                    self.selecaoDeMusica("anterior")
                case 7:
                    self.selecaoDeMusica("random")
                case 8:
                    pygame.mixer.music.stop()
                    self.indice = 0
                    self.menuSelecaoPlaylist()
                case 9:
                    self.limparTela()
                    print("\nÚltima música da playlist →", self.playlist_selecionada[self.indice])
                    input("\nPressione Enter para sair.")
                case _:
                    self.limparTela()
                    print("Opção inválida!")
                    self.timer(1)
                    self.playerMusicaMenu()
        self.StartMenu()

if __name__ == "__main__":
    music_player = MusicPlayer()
    music_player.StartMenu()
