


# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.button import Button

# class MyScreenApp(App):
#     def build(self):
#         sm = ScreenManager()
        
#         # Create a Screen w/1 button and add it
#         main = Screen(name='main')
#         main.add_widget(Button(text='main'))
#         sm.add_widget(main)
        
#         return sm
        
# if __name__ == '__main__':
#     MyScreenApp().run()

#https://kivy.org/doc/stable/tutorials/pong.html
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()