from kivymd.app import MDApp
from kivy.lang import Builder
from helper import KV;
<<<<<<< HEAD
from tkinter.filedialog import askopenfilename
from kivy.uix.image import Image
=======
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

>>>>>>> 07315d79e592dbfbd64c0d16f1ad5ce93977d41e

class DemoApp(MDApp):
    def build(self):
        # img = Image(source='cat.jpg')
        # return img
        return Builder.load_string(KV)
    def selectFile(self):
        filename = askopenfilename()
        print(filename)

DemoApp().run()
