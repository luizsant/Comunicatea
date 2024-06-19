import os

# Desabilitar clipboard completamente
os.environ["KIVY_NO_ARGS"] = "1"
os.environ["KIVY_CLIPBOARD"] = "none"

from kivy.config import Config
Config.set('kivy', 'log_level', 'debug')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='ComunicaTEA - Inclusão Digital para Crianças Autistas', font_size=24)
        self.add_widget(self.label)

        self.text_input = TextInput(hint_text='Digite uma mensagem')
        self.add_widget(self.text_input)

        self.send_button = Button(text='Enviar')
        self.send_button.bind(on_press=self.on_send_button_press)
        self.add_widget(self.send_button)

        self.output_label = Label(text='')
        self.add_widget(self.output_label)

    def on_send_button_press(self, _):
        message = self.text_input.text
        self.output_label.text = f'Mensagem enviada: {message}'
        self.text_input.text = ''

class ComunicaTEAApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    ComunicaTEAApp().run()
