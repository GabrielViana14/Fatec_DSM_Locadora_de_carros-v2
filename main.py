from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard

main_kv = '''

Screen:
    BoxLayout:
        orientation: 'vertical'
        BarraSuperior:
        TelaLogin:

<TelaLogin>:
    MDIconButton:
        pos_hint: {'center_x':.5,'center_y':.8}
        icon: 'language-python'
        icon_size: '75sp'
    MDTextField:
        hint_text: 'Email:'
        pos_hint: {'center_x':.5,'center_y':.6}
        size_hint_x: .7
    MDTextField:
        hint_text: 'Senha:'
        pos_hint: {'center_x':.5,'center_y':.45}
        size_hint_x: .7
    MDRaisedButton:
        text: 'Entrar'
        pos_hint: {'center_x':.5,'center_y':.35}
        size_hint_x: .7
    MDTextButton:
        text: 'Esqueceu sua senha?'
        pos_hint: {'center_x':.5,'center_y':.25}
        on_release: root.esqueci_senha()
    MDTextButton:
        text: 'Cadastrar'
        pos_hint: {'center_x':.5,'center_y':.20}
        on_release: root.cadastrar()

<BarraSuperior@MDTopAppBar>:
    title: 'login'
    anchor_title: "left"
    left_action_items: [["menu"]]
    elevation: 1

<EsqueciSenhaCard>:
    orientation: 'vertical'
    size_hint: .5,.7
    pos_hint: {'center_x':.5,'center_y':.5}
    elevation: 2
    radius: 4
    MDFloatLayout:
        MDLabel:
            font_style: 'H5'
            text: 'Lembrar Senha'
            halign: 'center'
            pos_hint: {'center_x':.5,'center_y':.8}
        MDTextField:
            hint_text: 'E-mail'
            size_hint_x: .7
            pos_hint: {'center_x':.5,'center_y':.5}
        MDTextField:
            hint_text: 'Nova Senha'
            size_hint_x: .7
            pos_hint: {'center_x':.5,'center_y':.4}
        MDTextField:
            hint_text: 'Confirmar nova senha'
            size_hint_x: .7
            pos_hint: {'center_x':.5,'center_y':.3}
        MDRaisedButton:
            text: 'Mudar Senha'
            pos_hint: {'center_x':.5,'center_y':.15}
            size_hint_x: .5
'''

class EsqueciSenhaCard(MDCard):
    ...

class TelaLogin(FloatLayout):
    def esqueci_senha(self):
        print("Abrindo tela de esqueci senha")
        self.add_widget(EsqueciSenhaCard())

    def cadastrar(self):
        print("Abrindo tela de cadastro")

class MyApp(MDApp):
    def build(self):

        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_string(main_kv)

MyApp().run()