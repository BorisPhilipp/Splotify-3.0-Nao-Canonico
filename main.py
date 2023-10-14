from Lista import Lista
from Menus import Menu
from Musica import Player

lista = Lista("musicastotais.txt")
menu = Menu()
player = Player(lista.lista_musicas)

menu.exibir_menu_principal()

def selecao_menu_principal():
    while True:
        menu.opcao = int(input("Digite uma opção: "))
        opcao = menu.opcao
        if opcao in (1,2,3):
            break
        print("Opcao invalida")

    if opcao == 1:
        print()
        lista.listar_musicas()
        player.selecaoPlaylist(int(input("\nDigite o numero correspondente a playlist: ")) - 1)
        player.tocarMusica()

    elif opcao == 2:
        print()
        lista.listar_musicas()
        input("\nPressione qualquer tecla para sair...")

    elif opcao == 3:
        menu.exibir_fim()
        exit()

selecao_menu_principal()