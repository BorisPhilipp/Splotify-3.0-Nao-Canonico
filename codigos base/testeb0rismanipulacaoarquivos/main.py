def lerMusicas(musicas):
    listaMusica = []

    with open(musicas, 'r') as arquivoMusicas:
        quantidade = len(arquivoMusicas.readlines())
    
    with open(musicas, 'r') as arquivoMusicas:
        arquivoMusicas.seek(0)
        
        contador = 1
        for i in range(int((quantidade/3))):
            listaBloco = []
            for j in range(1, 4):
                texto = arquivoMusicas.readline().strip()
                listaBloco.append(texto)
                if j == 3:
                    break
            listaMusica.append(listaBloco)
        print(listaMusica)
            
lerMusicas('musicastotais.txt') 