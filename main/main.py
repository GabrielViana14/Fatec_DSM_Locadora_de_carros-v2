from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from firebase import firebase

firebase = firebase.FirebaseApplication('https://projeto-fatec-locadora-default-rtdb.firebaseio.com/',None)

class TelaLogin(Screen):
    pass

class TelaCadastro(Screen):
    pass

class Principal(Screen):
    pass

class MyApp (MDApp):
    def build(self):
        kv_files = ['kv/main.kv', 'kv/TelaInicial.kv']
        for kv_file in kv_files:
            Builder.load_file(kv_file)

        screen_manager = ScreenManager()
        screen_manager.add_widget(TelaLogin(name='login'))
        screen_manager.add_widget(TelaCadastro(name='cadastro'))

        return screen_manager

    def cadastro(self):
        telacadastro = self.root.get_screen('cadastro')
        nome = telacadastro.ids.tf_nome
        email = telacadastro.ids.tf_email
        senha = telacadastro.ids.tf_senha
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

    def login(self):
        telalogin = self.root.get_screen('login')
        resultados = firebase.get('https://projeto-fatec-locadora-default-rtdb.firebaseio.com/Usuario', '')
        senha = telalogin.ids.tf_senha
        email = telalogin.ids.tf_email
        print(f'senha:{senha.text}\nEmail{email.text}')
        for i in resultados.keys():
            if resultados[i]['email'] == email.text:
                if resultados[i]['senha'] == senha.text:
                    print("Você está logado")
                    self.root.current = 'cadastro'



MyApp().run()