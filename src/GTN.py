# GTN - guess the number(угадай число)
# python version 3.10
# kivy 2.0.0

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class GTNApp(App):
    def build(self):
        return Main()

class Main(BoxLayout):
    pass

if __name__ == "__main__":
    GTNApp().run()
