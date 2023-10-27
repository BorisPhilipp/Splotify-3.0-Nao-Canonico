import Menus, Musica, os, time

class PlaylistSetup(Musica.Playlist):
    def __init__(self, arquivo_com_musicas):
        super().__init__(arquivo_com_musicas)
        self.separar_arquivo_em_lista()

    def verificadorOptionPlaylist(self):
        while True:
            user_input = int(input("Digite o número da playlist: "))
            
            if 0 <= user_input <= len(self._playlists_compactadas):
                self._playlist = self._playlists_compactadas[user_input]
                break
                    
            else:
                print("Playlist inválida!")
        
    
class OptionMenuUsuario:
    def verificadorOptionMenuPrincipal(self, arquivo_com_musicas):
        playlist_control = PlaylistSetup(arquivo_com_musicas)
        menus = Menus.Menus()

        while True:
            user_input = int(input("Digite uma opção: "))

            if user_input in (1,2,3):
                
                if user_input == 1:
                    apagarTela()
                    menus.printarPlaylists(playlist_control.arquivo)
                    playlist_control.verificadorOptionPlaylist()
                    break 
                
                elif user_input == 2:
                    apagarTela()
                    menus.printarPlaylists()
                    break
                
                elif user_input == 3:
                    break
                
            else:
                print("Opção inválida!")
                timer(1)
                apagarTela()
                Menus.Menus.printarMenuEscolhaPrincipal()


def apagarTela():
    os.system('clear' if os.name == 'posix' else 'CLS')


def timer(segundos):
    time.sleep(segundos)