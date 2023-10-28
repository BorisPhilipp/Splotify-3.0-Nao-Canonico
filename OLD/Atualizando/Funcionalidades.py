import os

class OptionMenuUsuario:
    def verificadorOptionMenuPrincipal():
        while True:
            user_input = int(input("Digite uma opção: "))
            if user_input in (1,2,3):
                if user_input == 1:
                    os.system("clear" if os.name == "posix" else "CLS")
                    print("musica")
                if user_input == 2:
                    os.system("clear" if os.name == "posix" else "CLS")
                    print("lista musica")
                if user_input == 3:
                    break
            else:
                print("Opção inválida!")