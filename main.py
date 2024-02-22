from kivymd.app import MDApp
from kivy.lang import Builder
#from helper import KV;
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

KV = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: "Profile"
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: "Upload"
        pos_hint: {'center_x': 0.5,'center_y': 0.2}
        on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: "Welcome"
        halign: "center"
    MDRectangleFlatButton:
        text: "Menu"
        pos_hint: {'center_x': 0.5,'center_y': 0.2}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: "Upload"
        halign: "center"
    MDRectangleFlatButton:
        text: "Menu"
        pos_hint: {'center_x': 0.5,'center_y': 0.2}
        on_press: root.manager.current = 'menu'

"""

Window.size = (500, 500)

    
class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm=ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(ProfileScreen(name="profile"))
sm.add_widget(UploadScreen(name="upload"))

class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

DemoApp().run()
