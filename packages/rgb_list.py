import statistics as st

class rgbList():    
    def __init__(self):
        self.listaR = []
        self.listaG = []
        self.listaB = []

    def appendNewRGB(self, r, g, b):
        self.listaR.append(r)
        self.listaG.append(g)
        self.listaB.append(b)

    def mode(self):
        return [st.mode(self.listaR), st.mode(self.listaG), st.mode(self.listaB)]
