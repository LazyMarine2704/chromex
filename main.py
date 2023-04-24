from packages.scan_image import scanImage

#instalando as bibliotecas necessárias
import subprocess
subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

#importar as bibliotecas
import cv2
import keyboard
import pyttsx3
import pandas as pd
import os

#Impotando base de dados das cores.
path = os.getcwd()

# Read CSV file at the beginning of the code
csv = pd.read_csv("colors.csv", names=["color","color_name","hex","R","G","B"], header=0)

#Open Camera
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
        cv2.imshow('Chromex', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        caminho = 'captura.jpg'
        cv2.imwrite(caminho, frame)
        captura = cv2.imread(caminho)
        captura = cv2.convertScaleAbs(captura,1)
        captura_rgb = cv2.cvtColor(captura, cv2.COLOR_BGR2RGB)
        captura_pronta = scanImage(captura_rgb, csv)

        engine = pyttsx3.init()
        engine.say(captura_pronta)
        engine.runAndWait()
        
    elif keyboard.is_pressed('q'):
        break

camera.release()
cv2.destroyWindow('Chromex')
exit()