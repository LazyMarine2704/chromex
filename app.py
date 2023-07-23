import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder  # Importe a classe Builder

class CameraAndRoundButtonLayout(RelativeLayout):
    pass

class MyRoundButton(Button):
    pass

class CameraAndRoundButtonApp(App):
    def build(self):
        # Carregue o arquivo KV com as informações de estilo
        Builder.load_file('styles.kv')
        
        # Crie um layout de caixa vertical para organizar os widgets
        layout = CameraAndRoundButtonLayout()
        
        # Crie o widget da câmera e adicione ao layout
        available_cameras = Camera.ids
        if available_cameras:
            camera = Camera(index=0, resolution=(640, 480), play=True)
            layout.add_widget(camera)
        else:
            layout.add_widget(Label(text="Nenhuma câmera disponível."))
        
        # Crie o botão redondo e adicione ao layout
        round_button = MyRoundButton(text="Clique", size_hint=(None, None), size=(100, 100))
        round_button.bind(on_release=self.on_button_click)
        layout.add_widget(round_button)

        return layout

    def on_button_click(self, instance):
        print("Botão Clicado!")

if __name__ == '__main__':
    CameraAndRoundButtonApp().run()