


# from kivy.app import App
# from kivy.uix.widget import Widget

# class MainWidget(Widget):
#     pass

# class TheLabApp(App):
#     def build(self):
#         return MainWidget() 

# TheLabApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TheLab(BoxLayout):
    def say_hello(self):
        print("hello")

class TheLabApp(App):
    def build(self):
        return TheLab()

if __name__ == "__main__":
    TheLabApp().run()
