# GTN - guess the number(угадай число)
# python version 3.10
# kivy 2.0.0

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
import random
import time


score = 0



class Main(Widget):
    datainput = ObjectProperty()
    answer = ObjectProperty()
    enter = ObjectProperty()
    score = ObjectProperty()
    records = ObjectProperty()
    help = ObjectProperty()
    score1 = 1

    def update_data1(self):
        self.data1.text = str(time.ctime())
        Clock.schedule_interval(self.Callback_Clock, 1)


    def Callback_Clock(self, dt):
        self.data1.text = str(time.ctime())


    def random_number(self):
        rm = str(random.randint(1,10))
        self.score.text = str(score)
        if self.datainput.text == rm:
            self.answer.text = 'Верно ' + str(rm)
        else:
            self.answer.text = 'Неверно ' + str(rm)

class GTNApp(App):
    def build(self):
        return Main()


if __name__ == '__main__':
    GTNApp().run()
