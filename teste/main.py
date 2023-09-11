from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard

class MyApp(MDApp):
    def build(self):
        main_kv = Builder.load_file('main.kv')
        self.theme_cls.primary_palette = "Indigo"
        return main_kv

MyApp().run()