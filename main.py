from kivymd.app import MDApp
from kivy.lang import Builder
from helper import KV;
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

DemoApp().run()
