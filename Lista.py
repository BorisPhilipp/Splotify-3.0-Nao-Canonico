class Fabricador:
    def __init__(self, playlist, listaMusica=[]):
        self._playlist = playlist
        self._listaMusica = listaMusica

    def lerMusicas(self):

        with open(self._playlist, 'r') as arquivoMusicas:
            quantidade = len(arquivoMusicas.readlines())
        
        with open(self._playlist, 'r') as arquivoMusicas:
            arquivoMusicas.seek(0)
            
            contador = 1
            for i in range(int((quantidade/3))):
                listaBloco = []
                for j in range(1, 4):
                    texto = arquivoMusicas.readline().strip()
                    listaBloco.append(texto)
                    if j == 3:
                        break
                self._listaMusica.append(listaBloco)


class Lista(Fabricador):
    def __init__(self, playlist):
        super().__init__(playlist)
    
    def escreve(self):
        self.lerMusicas()
        print(self._listaMusica)
