from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        button1 = Button(text='Расчет режимов резания')
        button1.bind(on_press=self.button_pressed)
        layout.add_widget(button1)

        self.add_widget(layout)

    def button_pressed(self, instance):
        if instance.text == 'Расчет режимов резания':
            self.parent.current = 'WorkingModes'


class WorkingModeScreen(Screen):
    def __init__(self, **kwargs):
        super(WorkingModeScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        working_modes = ['Резьба', 'Фрезерование', 'Сверление', 'Тончение', 'Центрирование', 'Центровка',
                         'Развертывание']

        for mode in working_modes:
            button = Button(text=mode)
            button.bind(on_press=self.button_pressed)
            layout.add_widget(button)

        back_button = Button(text='Назад')
        back_button.bind(on_press=self.back_button_pressed)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def button_pressed(self, instance):
        print(f'Вы выбрали режим работы {instance.text}')

    def back_button_pressed(self, instance):
        self.parent.current = 'main'

class TestApp(App):
    def build(self):
        screen_manager = ScreenManager()

        main_screen = MainScreen(name='main')
        screen_manager.add_widget(main_screen)

        working_mode_screen = WorkingModeScreen(name='WorkingModes')
        screen_manager.add_widget(working_mode_screen)

        return screen_manager

if __name__ == '__main__':
    TestApp().run()
