from kivymd.app import MDApp
from kivy.lang import Builder
from helper import KV;
from tkinter.filedialog import askopenfilename
from kivy.uix.image import Image

class DemoApp(MDApp):
    def build(self):
        # img = Image(source='cat.jpg')
        # return img
        return Builder.load_string(KV)
    def selectFile(self):
        filename = askopenfilename()
        print(filename)

DemoApp().run()
