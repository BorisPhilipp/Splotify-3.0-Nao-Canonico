import Menus, os, time

class OptionMenuUsuario:

    def verificadorOptionMenuPrincipal():
        while True:
            user_input = int(input("Digite uma opção: "))

            if user_input in (1,2,3):

                if user_input == 1:
                    apagarTela()
                    Menus.Menus.printarPlaylists("musicastotais.txt")
                    
                if user_input == 2:
                    apagarTela()
                    print("lista musica")
                    
                if user_input == 3:
                    break

            else:
                print("Opção inválida!")
                apagarTela()
                Menus.Menus.printarMenuEscolhaPrincipal()


def apagarTela():
    os.system('clear' if os.name == 'posix' else 'CLS')


def timer(segundos):
    time.sleep(segundos)