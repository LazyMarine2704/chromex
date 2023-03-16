import cv2
import numpy as np
import pyttsx3
import keyboard

# Iniciar e Configurar voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


# Inicializa a câmera
cap = cv2.VideoCapture(0)

while True:
    # Captura um quadro da câmera
    ret, frame = cap.read()

    # Exibe o quadro na tela
    cv2.imshow('frame', frame)

    # Espera pela tecla 's' para salvar a fotografia
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Salva a fotografia em um arquivo
        cv2.imwrite('foto.png', frame)
        
        # Converte a imagem para o espaço de cores HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Calcula o histograma de cores para o canal H (matiz)
        hist = cv2.calcHist([hsv], [0], None, [180], [0, 180])
        
        # Encontra a cor predominante
        cor_predominante = np.argmax(hist)
        
        # Exibe a cor predominante na tela
		#Cor Vermelha
        print("Cor predominante:", cor_predominante)
        if cor_predominante <15 or cor_predominante >165:
            print("Vermelho") 
            engine.say('Vermelho')
            engine.runAndWait()
        
		#Cor Laranja
        elif cor_predominante <25:
            print("Laranja")
            engine.say("Laranja")
            engine.runAndWait()
 
		#Cor Amarelo
        elif cor_predominante < 45:
            print("Amarelo")
            engine.say('Amarelo')
            engine.runAndWait()
            
		#Cor Verde
        elif cor_predominante < 75: #verde
            print("Verde")
            engine.say('Verde')
            engine.runAndWait()

		 #Cor Azul Claro   
        elif cor_predominante < 105: #azul claro
            print("Azul claro")
            engine.say('Azul claro')
            engine.runAndWait()
        
		#Cor Azul Escuro
        elif cor_predominante < 135: #azul escuro
            print("Azul escuro")
            engine.say('Azul escuro')
            engine.runAndWait()

		#Cor Rosa
        elif cor_predominante < 165: #rosa
            print("Rosa")
            engine.say('Rosa')
            engine.runAndWait()	      

    if keyboard.is_pressed('q'):
        break

# Libera a câmera e fecha a janela
cap.release()
cv2.destroyAllWindows()
