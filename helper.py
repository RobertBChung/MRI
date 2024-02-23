KV = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
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

