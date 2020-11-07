from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layourt = BoxLayout(orientation='vertical')
        label1 = Label(text='Hello word')
        label2 = Label(text='label 2')

        button1 = Button(text='Button 1')
        button2 = Button(text='Button 2', color='purperl')

        layourt.add_widget(label1)
        layourt.add_widget(label2)
        layourt.add_widget(button1)
        layourt.add_widget(button2)
        # return Button(text='Hello world')

        return layourt


if __name__ == '__main__':
    MyApp().run()
