from kivymd.app import MDApp
from kivy.lang import Builder
from kivy_garden.mapview import MapView

class Mapview(MapView):
    pass


class MyApp (MDApp):
    def build(self):
        kv = Builder.load_file('kv/map.kv')
        return kv

MyApp().run()
