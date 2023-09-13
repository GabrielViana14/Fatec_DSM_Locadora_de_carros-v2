from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard

class EsqueciSenhaCard(MDCard):
    ...

    
class MyApp(MDApp):
    def build(self):
        main_kv = Builder.load_file('kv/TelaLogin.kv')
        self.theme_cls.primary_palette = "Indigo"
        return main_kv

    def esqueci_senha(self):
        print("Abrindo tela de esqueci senha")
        self.add_widget(EsqueciSenhaCard())

    def cadastrar(self):
        print("Abrindo tela de cadastro")

MyApp().run()
