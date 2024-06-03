import cv2
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from chromex import (
    Chromex,
)  # Certifique-se de que o módulo chromex seja importado corretamente

Builder.load_string("""
<CameraApp>:
    orientation: 'vertical'

    Camera:
        id: kivy_camera  # Altere o nome da propriedade para evitar conflitos
        resolution: (640, 480)

    Button:
        text: 'Capturar Imagem'
        on_release: root.capture_image()
""")


class CameraButton(Button):
    pass


class CameraApp(App):
    chromex = None  # Defina chromex como uma variável de classe

    def build(self):
        self.chromex = Chromex(
            "chromex/data/captura.png", "chromex/data/colors.csv"
        )  # Inicialize chromex no método build
        layout = BoxLayout(orientation="vertical")

        Builder.load_file("styles.kv")  # Carrega o arquivos de estilos do Kivy.

        # Crie o widget da câmera e adicione ao layout
        self.camera = Camera(index=0, resolution=(640, 480), play=True)
        layout.add_widget(self.camera)

        # Botão para capturar a imagem
        capture_button = CameraButton(text="Capturar Imagem")
        capture_button.bind(
            on_press=self.button_press
        )  # Esta bind chama a função capture_image quando o evento de botão for detectado.
        layout.add_widget(capture_button)

        return layout

    def button_press(self, *args):
        filename = self.chromex.filename
        self.camera.export_to_png(filename)
        captura = cv2.imread(filename)
        captura = cv2.convertScaleAbs(captura, 1)
        captura = cv2.cvtColor(captura, cv2.COLOR_BGR2RGB)
        cor = self.chromex.getColorName(captura)
        self.chromex.sayColorName(cor)


if __name__ == "__main__":
    CameraApp().run()
