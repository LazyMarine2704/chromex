import cv2
import keyboard
import pyttsx3
import numpy as np
import pandas as pd

#Impotando base de dados das cores.
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('C://Projetos/chromex/assets/database/colors.csv', names=index, header=None)

#Calcula a distância para definir a cor
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

def scanImage(imagem):
    # Obtém as dimensões da imagem
    height, width, channels = imagem.shape
    print(height, width, channels)

    # Percorre cada pixel da imagem e imprime seus valores RGB.
    for i in range(height):
        for j in range(width):
            r, g, b = imagem[i, j]

    captura_escaneada = getColorName(r, g, b)

    return captura_escaneada
    

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