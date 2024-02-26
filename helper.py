KV = KV = '''
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
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
