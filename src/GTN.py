# GTN - guess the number(угадай число)
# python version 3.10
# kivy 2.0.0

from kivy.app import App
from kivy.uix.widget import Widget


class Main(Widget):
    pass


class GTNApp(App):
    def build(self):
        return Main()


if __name__ == '__main__':
    GTNApp().run()
