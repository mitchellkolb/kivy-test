


# from kivy.app import App
# from kivy.uix.widget import Widget

# class MainWidget(Widget):
#     pass

# class TheLabApp(App):
#     def build(self):
#         return MainWidget() 

# TheLabApp().run()

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

class MyScreenApp(App):
    def build(self):
        sm = ScreenManager()
        
        # Create a Screen w/1 button and add it
        main = Screen(name='main')
        main.add_widget(Button(text='main'))
        sm.add_widget(main)
        
        return sm
        
if __name__ == '__main__':
    MyScreenApp().run()