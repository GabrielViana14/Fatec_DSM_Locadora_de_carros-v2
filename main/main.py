from kivymd.app import MDApp
from kivy.lang import Builder

class MyApp (MDApp):
    def build(self):
        main_kv = Builder.load_file('kv/TelaInicial.kv')

        return main_kv

MyApp().run()