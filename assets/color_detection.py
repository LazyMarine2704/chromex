import cv2
import keyboard
import pyttsx3
import numpy as np
import pandas as pd
from scipy import stats
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
csv = pd.read_csv("../chromex/assets/database/colors.csv", names=index, header=0)

def scanImage(imagem):
    lista = rgbList()
    height, width, channels = imagem.shape
    print(height, width, channels)

    # Runs through each pixel of the image and returns each RGB value
    for i in range(height):
        for j in range(width):
            r, g, b = imagem[i,j]
            lista.appendNewRGB(r, g, b)
    
    cor = lista.mode()
    print(getColorName(cor[0], cor[1], cor[2]))
    print(cor[0], cor[1], cor[2])

    return getColorName(cor[0], cor[1], cor[2])
    
#Open Camera
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
        cv2.imshow('Chromex', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        caminho = '../chromex/assets/images/captura.jpg'
        cv2.imwrite(caminho, frame)
        captura = cv2.imread(caminho)
        captura = cv2.convertScaleAbs(captura,1)
        captura_rgb = cv2.cvtColor(captura, cv2.COLOR_BGR2RGB)
        captura_pronta = scanImage(captura_rgb)

        #Voice module
        engine = pyttsx3.init()
        engine.say(captura_pronta)
        engine.runAndWait()
    
    elif keyboard.is_pressed('q'):
        break

camera.release()
cv2.destroyWindow('Chromex')
exit()