from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from firebase import firebase
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.toast import toast
import os
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.menu import MDDropdownMenu
import pyrebase
from plyer import gps


config = {
    'apiKey': "AIzaSyD-s8_15tuIkyV0DvAp2lnBoFx9e0cX87k",
    'authDomain': "projeto-fatec-locadora.firebaseapp.com",
    'databaseURL': "https://projeto-fatec-locadora-default-rtdb.firebaseio.com",
    'projectId': "projeto-fatec-locadora",
    'storageBucket': "projeto-fatec-locadora.appspot.com",
    'messagingSenderId': "428810569718",
    'appId': "1:428810569718:web:cd755ea98ed5be2efba9d7",
    'measurementId': "G-ECR55G0KD3"

}
firebase_init = pyrebase.initialize_app(config)
storage = firebase_init.storage()

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.latitude = None
        self.longitude = None
    def get_location(self, *args):
        #Inicia localização GPS
        try:
            gps.configure(on_location=self.on_gps_location)
            gps.start(minTime=1000, minDistance=1)
        except:
            print("Gps não está disponivel")

    def on_gps_location(self, **kwargs):
        self.latitude = kwargs['lat']
        self.longitude = kwargs['lon']
        print(f'Latitude {self.latitude}, Longitude {self.longitude}')
    def cadastro(self):   #Envia cadastro de carros para o banco firebase
        categoria = self.ids.tf_categoria
        modelo = self.ids.tf_modelo
        placa = self.ids.tf_placa
        ano = self.ids.tf_ano
        cor = self.ids.tf_cor
        combustivel = self.ids.tf_combustivel
        preco = self.ids.tf_preco
        print(f"Categoria: {categoria.text}\n"
              f"Modelo: {modelo.text}\n"
              f"Placa: {placa.text}\n"
              f"Ano: {ano.text}\n"
              f"Cor: {cor.text}\n"
              f"Combustivel: {combustivel.text}\n"
              f"Latitude: {self.latitude}\n"
              f"Longitude: {self.longitude}")
        local_arquivo = self.ids.btn_enviar.text   #esse botão está com o local do arquivo
        destino_arquivo = f'imagens/{self.ids.tf_modelo.text}-{self.ids.tf_placa.text}' #aqui é onde o arquivo está guardado
        storage.child(destino_arquivo).put(local_arquivo)
        foto_url = storage.child(destino_arquivo).get_url(None)   #essa variavel pega o url da onde o arquivo está guardado
        print(f"Arquivo enviado com sucesso para o Firebase Storage: {foto_url}")


        data = {
            'Categoria': categoria.text,
            'Modelo': modelo.text,
            'Placa': placa.text,
            'Ano': ano.text,
            'Cor': cor.text,
            'Combustivel': combustivel.text,
            'Preço': preco.text,
            'Foto': foto_url,
            'Latitude': self.latitude,
            'Longitude': self.longitude
        }
        #procura na tabela Carros se já tem algum carro com a placa cadastrada e se não tiver ele cadastra
        resultados = firebase.get('https://projeto-fatec-locadora-default-rtdb.firebaseio.com/Carros','')
        for i in resultados.keys():
            if resultados[i]['Placa'] == placa.text:
                print("Placa já cadastrada")
            else:
                firebase.post('https://projeto-fatec-locadora-default-rtdb.firebaseio.com/Carros', data)

    def escolher_categoria(self):   #Escolhe a categoria do carro por meio de uma lista abaixo
        print('Escolhendo')
        menu_itens = [{  #itens da lista
            'text': 'Carro grande',
            'viewclass':"OneLineListItem",
            'on_release': lambda x= "Carro Grande": self.menu_retorno(x)
                       },{
            'text': 'Carro pequeno',
            'viewclass': "OneLineListItem",
            'on_release': lambda x= "Carro Pequeno": self.menu_retorno(x)
                       },
                    ]
        self.menu = MDDropdownMenu( #cria a lista
            caller=self.ids.tf_categoria, items=menu_itens,width_mult=4
        )
        self.menu.open()  #mostra a lista na tela

    def menu_retorno(self,txt_item): # muda o texto do textfield de categorias para o item escolhido
        self.ids.tf_categoria.text = txt_item
        self.menu.dismiss()
        print(f'o item escolhido {txt_item}')

    def escolher_combustivel(self): #Escolhe o tipo de combustivel do carro por meio de uma lista abaixo
        print('Escolhendo')
        menu_itens = [{    #itens da lista
            'text': 'Gasolina',
            'viewclass': "OneLineListItem",
            'on_release': lambda x="Gasolina": self.menu_retorno_combustivel(x)
        },{
            'text': 'Flex',
            'viewclass': "OneLineListItem",
            'on_release': lambda x="Flex": self.menu_retorno_combustivel(x)
        },
            {
                'text': 'Diesel',
                'viewclass': "OneLineListItem",
                'on_release': lambda x="Diesel": self.menu_retorno_combustivel(x)
            },{
            'text': 'Eletricidade',
            'viewclass': "OneLineListItem",
            'on_release': lambda x="Eletricidade": self.menu_retorno_combustivel(x)
        },
        ]
        self.menu = MDDropdownMenu(   #cria a lista
            caller=self.ids.tf_combustivel, items=menu_itens, width_mult=4
        )
        self.menu.open()  #mostra a lista na tela
    def menu_retorno_combustivel(self,txt_item):  # muda o texto do textfield de combustivel para o item escolhido
        self.ids.tf_combustivel.text = txt_item
        self.menu.dismiss()
        print(f'o item escolhido {txt_item}')

    def ir_cadastro(self):
        self.manager.current = 'cadastro'

    def ir_mapa(self):
        self.manager.current = 'mapa'

    def enviar_foto(self): #cria um explorador de arquivos
        self.manager_open = False
        path = os.path.expanduser('/')
        self.filemanager= MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )
        self.filemanager.show(path) #abre o explorador de arquivo

    def select_path(self, path: str):  #seleciona o arquivo ou pasta e fecha o explorador, botão usado para entrar tem o texto trocado pelo local do arquivo
        self.exit_manager()
        self.ids.btn_enviar.text = path
        toast(path)

    def exit_manager(self, *args): #fecha
        self.manager_open = False
        self.filemanager.close()



class Principal(Screen):
    pass

class Mapa(Screen):

    def ir_cadastro(self):
        self.manager.current = 'cadastro'

    def ir_mapa(self):
        self.manager.current = 'mapa'


class MyApp (MDApp):
    def build(self):
        kv_files = ['kv/login.kv', 'kv/cadastro.kv','kv/map.kv','kv/map.kv']
        for kv_file in kv_files:
            Builder.load_file(kv_file)
        screen_manager = ScreenManager()
        screen_manager.add_widget(Mapa(name='mapa'))
        screen_manager.add_widget(TelaLogin(name='login'))
        screen_manager.add_widget(TelaCadastro(name='cadastro'))
        screen_manager.add_widget(Principal(name='inicio'))


        return screen_manager









MyApp().run()