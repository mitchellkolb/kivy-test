


from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

class TheLabApp(App):
    def build(self):
        return MainWidget() 

TheLabApp().run()
