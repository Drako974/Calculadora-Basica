from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Parte superior: pantalla
        self.display = TextInput(
            readonly=True,
            halign='right',
            font_size=55,
            size_hint_y=0.2  # Ocupa el 20% de la altura
        )
        self.add_widget(self.display)

        # Parte inferior: botones
        botones = GridLayout(cols=4)

        for texto in [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]:
            btn = Button(text=texto, font_size=32)
            # Si el botón es un número, color negro con texto blanco
            if texto.isdigit():
                btn.background_color = (0, 0, 0, 1)  # Negro
                btn.color = (1, 1, 1, 1)  # Blanco
            # Si el botón es un operador, color naranja con texto blanco
            elif texto in ['+', '-', '*', '/']:
                btn.background_color = (1, 0.5, 0, 1)  # Naranja
                btn.color = (1, 1, 1, 1)  # Blanco
            btn.bind(on_press=self.on_button_press)
            botones.add_widget(btn)

        self.add_widget(botones)

    def on_button_press(self, instance):
        texto = instance.text
        if texto == 'C':
            self.display.text = ''
        elif texto == '=':
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = 'Error'
        else:
            self.display.text += texto

class MiApp(App):
    def build(self):
        return Calculadora()

if __name__ == "__main__":
    MiApp().run()