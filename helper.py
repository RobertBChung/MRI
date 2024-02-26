<<<<<<< HEAD
KV = KV = '''
=======
KV = """
>>>>>>> 07315d79e592dbfbd64c0d16f1ad5ce93977d41e
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
<<<<<<< HEAD
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Demo"
                        md_bg_color: .2, .2, .2, 1
                        specific_text_color: 1, 1, 1, 1
                    MDBoxLayout:
                        orientation: "horizontal"
                        MDBoxLayout:
                            orientation: 'vertical'
                            Image:
                                source: "cat.jpg"
                        MDBoxLayout:
                            orientation: 'vertical'
                            MDLabel: 
                                text:"hello"
                                halign: "center"
                    MDBottomAppBar:
                        id: bottom_appbar
                        allow_hidden: True
                        theme_bg_color: "Custom"
                        md_bg_color: "#232217"
                        halign: "center"
                        MDFabBottomAppBarButton:
                            id: fab_button
                            icon: "plus"
                            halign: "center"
                            theme_bg_color: "Custom"
                            md_bg_color: "#373A22"
                            theme_icon_color: "Custom"
                            icon_color: "#ffffff"
                            on_press: app.selectFile()
'''
=======
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Demo Application"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 5
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
"""

>>>>>>> 07315d79e592dbfbd64c0d16f1ad5ce93977d41e
