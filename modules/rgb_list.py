class rgbList():    
    def __init__(self):
        self.listaR = []
        self.listaG = []
        self.listaB = []

    # Insere os valores de cada canal em sua lista respectiva.
    def appendNewRGB(self, r, g, b):
        self.listaR.append(r)
        self.listaG.append(g)
        self.listaB.append(b)