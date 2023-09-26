from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from firebase import firebase

firebase = firebase.FirebaseApplication('https://projeto-fatec-locadora-default-rtdb.firebaseio.com/',None)

class TelaLogin(Screen):
    def login(self):
        resultados = firebase.get('https://projeto-fatec-locadora-default-rtdb.firebaseio.com/Usuario', '')
        senha = self.ids.tf_senha
        email = self.ids.tf_email
        print(f'senha:{senha.text}\nEmail{email.text}')
        for i in resultados.keys():
            if resultados[i]['email'] == email.text:
                if resultados[i]['senha'] == senha.text:
                    print("Você está logado")
                    self.manager.current = 'cadastro'

    def ir_cadastro(self):
        self.manager.current = 'cadastro'

class TelaCadastro(Screen):
    def cadastro(self):
        nome = self.ids.tf_nome
        email = self.ids.tf_email
        senha = self.ids.tf_senha
        print(f"nome: {nome.text}\n E-mail: {email.text}\nSenha: {senha.text}")
        data = {
            'nome': nome.text,
            'email': email.text,
            'senha': senha.text
        }

        resultados = firebase.get('https://projeto-fatec-locadora-default-rtdb.firebaseio.com/Usuario','')

        for i in resultados.keys():
            if resultados[i]['email'] == email.text:
                print("email já cadastrado")
            else:
                firebase.post('https://projeto-fatec-locadora-default-rtdb.firebaseio.com/Usuario', data)

class Principal(Screen):
    pass

class MyApp (MDApp):
    def build(self):
        kv_files = ['kv/login.kv', 'kv/cadastro.kv','kv/testes.kv']
        for kv_file in kv_files:
            Builder.load_file(kv_file)

        screen_manager = ScreenManager()
        screen_manager.add_widget(TelaLogin(name='login'))
        screen_manager.add_widget(TelaCadastro(name='cadastro'))
        screen_manager.add_widget(Principal(name='inicio'))

        return screen_manager





MyApp().run()