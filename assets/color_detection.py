import cv2
import keyboard
import pyttsx3
import numpy as np
import pandas as pd

class rgbList():    
    def __init__(self):
        self.listaR = []
        self.listaG = []
        self.listaB = []

    def appendNewRGB(self, r, g, b):
        self.listaR.append(r)
        self.listaG.append(g)
        self.listaB.append(b)

    def media(self):
        return [np.average(self.listaR), np.average(self.listaG), np.average(self.listaB)]

def getColorName(r, g, b):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(r- int(csv.loc[i,"R"])) + abs(g- int(csv.loc[i,"G"]))+ abs(b- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname 

#Impotando base de dados das cores.
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('C://Projetos/chromex/assets/database/colors.csv', names=index, header=0)

def scanImage(imagem):
    lista = rgbList()
    height, width, channels = imagem.shape
    print(height, width, channels)

    # Percorre cada pixel da imagem e imprime seus valores RGB.
    for i in range(height):
        for j in range(width):
            r, g, b = imagem[i,j]
            lista.appendNewRGB(r, g, b)
    
    cor = lista.media()
    print(cor[0], cor[1], cor[2])
    print(getColorName(round(cor[0]), round(cor[1]), round(cor[2])))
    return getColorName(round(cor[0]), round(cor[1]), round(cor[2]))
    
#Inicia a câmera
camera = cv2.VideoCapture(0)

while True:
    #captura os frames da câmera
    ret, frame = camera.read()

    #mostra os frames capturados na tela 
    if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
        cv2.imshow('Chromex', frame)

    #espera pela tecla 's'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        #define o caminho onde salvar a captura de tela
        caminho = 'C://Projetos/chromex/assets/images/captura.jpg'
        #armazena a captura em uma variável, e a converte para um formato compreensível ao cv2
        cv2.imwrite(caminho, frame)
        captura = cv2.imread(caminho)
        captura = cv2.convertScaleAbs(captura,1)
        #converte a captura de tela para o formato rgb
        captura_rgb = cv2.cvtColor(captura, cv2.COLOR_BGR2RGB)
        print('CONVERSÃO BEM SUCEDIDA')
        captura_pronta = scanImage(captura_rgb)

        #Sistema de voz
        engine = pyttsx3.init()
        engine.say(captura_pronta)
        engine.runAndWait()
    
    elif keyboard.is_pressed('q'):
        break

camera.release()
cv2.destroyWindow('Chromex')
exit()