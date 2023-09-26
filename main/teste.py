from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.pickers import MDDatePicker
import datetime

global id_btn

class MyApp (MDApp):
    def build(self):
        main = Builder.load_file('kv/cadastro.kv')

        return main



    def fechar_date_inicio(self, instance, value):
        self.root.ids.btn_data_inicio.text = 'De:'

    def select_date_inicio(self, id):
        date_dialog = MDDatePicker(year=datetime.date.today().year,month=datetime.date.today().month,day=datetime.date.today().day)
        date_dialog.bind(on_save=lambda instance, value, data_range:  self.salvar_data_inicio(id, value, data_range), on_cancel=self.fechar_date_inicio)
        date_dialog.open()

    def salvar_data_inicio(self, btn_id, value, data_range):
            btn = self.root.ids.btn_data_inicio
            btn.text = f"De: {value}"

    def fechar_date_fim(self, instance, value):
        self.root.ids.btn_data_fim.text = 'Até'

    def select_date_fim(self, id):
        date_dialog = MDDatePicker(year=datetime.date.today().year,month=datetime.date.today().month,day=datetime.date.today().day)
        date_dialog.bind(on_save=lambda instance, value, data_range:  self.salvar_data_fim(id, value, data_range), on_cancel=self.fechar_date_fim)
        date_dialog.open()

    def salvar_data_fim(self, btn_id, value, data_range):
            btn = self.root.ids.btn_data_fim
            btn.text = f"De: {value}"

MyApp().run()