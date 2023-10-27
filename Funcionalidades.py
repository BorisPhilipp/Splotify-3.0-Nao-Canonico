import Menus, Musica, os, time       
    
class OptionMenuUsuario:
    def verificadorOptionMenuPrincipal(self, arquivo_com_musicas):
        playlist_control = Musica.PlaylistSetup(arquivo_com_musicas)
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