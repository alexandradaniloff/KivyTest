from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Happy(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        #self.window.add_widget(
        #    Image(source="source/image.ipg")
        #)


        self.conngrat = Label(text='Введите имя')
        self.window.add_widget(self.conngrat)

        self.input_name = TextInput(
            size_hint=(1, 0.2),
            multiline =False,
            padding=(20)
        )
        self.window.add_widget(self.input_name)

        self.button = Button(
            text = "Поздравить",
            size_hint = (1, 0.3),
        )
        self.window.add_widget(self.button)

        self.button.bind(on_press=self.change_text)

        #return Image(source="source/image.jpg")

        return self.window

    def change_text(self, instance):
        self.conngrat.text='Поздравляю,'+self.input_name.text + '!'

if __name__ == '__main__':
    Happy().run()