import cv2
import pandas as pd
import pyttsx3
import keyboard
import time

class Chromex:
    def __init__(self, filename, csv) -> None:
        
        '''
        Inicializa a instância do Chromex e as funções de reconhecimento de
        cor.
        '''

        self.filename = filename
        self.csv = pd.read_csv(csv, names=["color","color_name","hex","R","G","B"], header=0)

    def capturarImagem(self):
        screen = cv2.VideoCapture(0)
        screen.set(10, 0.5)  # Ajusta o balanço de branco (0.5 é o valor médio)
        screen.set(15, -2)   # Ajusta a exposição (-2 é um valor de exposição padrão)


        # Tenta recuperar um frame da câmera e exibir na tela
        try:
            while True:
                ret, frame = screen.read()
                cv2.imshow('frame', frame)
                cv2.waitKey(1)

                if keyboard.is_pressed('s'):
                    print('Tecla s pressionada')
                    cv2.imwrite(self.filename, frame)
                    captura = cv2.imread(self.filename)
                    captura = cv2.convertScaleAbs(captura, 1)
                    captura = cv2.cvtColor(captura, cv2.COLOR_BGR2RGB)
                    time.sleep(1)
                    return captura

                if keyboard.is_pressed('q'):
                    screen.release()
                    cv2.destroyAllWindows()
                    break

        except cv2.error as e:
            print(e)

    def getColorName(self, image) -> str:
        height, width, _ = image.shape

        # Calcula o retângulo central
        central_height = int(height * 0.1)
        central_width = int(width * 0.1)
        central_top = int(height * 0.45)
        central_left = int(width * 0.45)

        # Calcula a média de cada canal no retângulo central
        r = int(image[
            central_top:central_top + central_height,
            central_left:central_left + central_width, 0
        ].mean())

        g = int(image[
            central_top:central_top + central_height,
            central_left:central_left + central_width, 1
        ].mean())

        b = int(image[
            central_top:central_top + central_height,
            central_left:central_left + central_width, 2
        ].mean())

        try:
            limiar = 75
            minimum_distance = float('inf')
            recognized_color = None

            for i in range(len(self.csv)):
                r_csv = int(self.csv.loc[i, "R"])
                g_csv = int(self.csv.loc[i, "G"])
                b_csv = int(self.csv.loc[i, "B"])

                distance = ((r - r_csv) ** 2 +
                            (g - g_csv) ** 2 +
                            (b - b_csv) ** 2) ** 0.5

                if distance < minimum_distance:
                    minimum_distance = distance
                    recognized_color = self.csv.loc[i, "color_name"]

            # Adicione um limiar de distância para evitar correspondências incorretas
            if minimum_distance <= limiar:
                return recognized_color
            else:
                return "Cor desconhecida"

        except Exception as e:
            print(e)


    def sayColorName(self, color_name):
        engine = pyttsx3.init()
        engine.say(color_name)
        print(color_name)
        engine.runAndWait()

if __name__ == '__main__':
    while True:
        # Crie uma instância da classe Chromex
        chromex = Chromex('captura.jpg', 'colors.csv')

        # Captura a imagem
        captura = chromex.capturarImagem()

        # Obtém o nome da cor
        color_name = chromex.getColorName(captura)

        # Diz o nome da cor
        chromex.sayColorName(color_name)
