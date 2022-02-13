#GTN - guess the number(угадай число)
#python version 3.10
#kivy 2.0.0

from kivy.app import App
from kivy.config import Config

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class GTNApp(App):
    def build(self):
        self.input = ''
        main = BoxLayout(orientation='vertical', )  # Лейбл основного окна

        top = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        center = BoxLayout(orientation='vertical', size_hint=(1, 0.4))
        bot = GridLayout(cols=3, size_hint=(1, 0.5))

        main.add_widget(top)
        main.add_widget(center)
        main.add_widget(bot)
        return main






if __name__ == "__main__":
    GTNApp().run()


