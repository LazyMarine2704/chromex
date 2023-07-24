from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from packages.scan_image import scanImage
import cv2
import kivy
import pandas as pd
import pyttsx3
kivy.config.Config.set('kivy', 'log_level', 'critical')

# Base de dados de valores RGB
csv = pd.read_csv("colors.csv", names=["color","color_name","hex","R","G","B"], header=0)

class CameraButton(Button):
    pass

class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        Builder.load_file('styles.kv') # Carrega o arquivos de estilos do Kivy.

        # Crie o widget da câmera e adicione ao layout
        self.camera = Camera(index=0, resolution=(640, 480), play=True)
        layout.add_widget(self.camera)

        # Botão para capturar a imagem
        capture_button = CameraButton(text="Capturar Imagem")
        capture_button.bind(on_press=self.capture_image) #Esta bind chama a função capture_image quando o evento de botão for detectado.
        layout.add_widget(capture_button)

        return layout

    def capture_image(self, *args):

        # Salva a textura da câmera em um arquivo "captura.jpg"
        filename = "captura.jpg"
        self.camera.export_to_png(filename)

        # Processo de conversão de imagem, do padrão BGR para o RGB
        captura = cv2.imread("captura.jpg")
        captura = cv2.convertScaleAbs(captura, 1)
        captura_rgb = cv2.cvtColor(captura, cv2.COLOR_BGR2RGB)
        captura_pronta = scanImage(captura_rgb, csv) # Ver módulos "scan_image.py" e "get_color_name.py".

        # Módulo de voz
        engine = pyttsx3.init()
        engine.say(captura_pronta)
        engine.runAndWait()

if __name__ == '__main__':
    CameraApp().run()