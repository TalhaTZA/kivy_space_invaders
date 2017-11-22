from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.clock import Clock
from fleet import Fleet
from shooter import Shooter
from kivy.core.audio import SoundLoader

Builder.load_file('images.kv')

class Invasion(FloatLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self.close,self)
        self._keyboard.bind(on_key_down=self.press)
        self.start_game()
    
    def close(self):
        self._keyboard.unbind(on_key_down = self.press)
        self._keyboard=None
    
    def press(self,keyboard,keycode,text,modifiers):
        if keycode[1]== 'left' and self.shooter.x > 10:
            self.shooter.center_x -=30
        elif keycode[1] == 'right'and self.shooter.x<self.parent.width - 50 :
            self.shooter.center_x +=30
        return True
    
    def start_game(self):
        label = Label(text='Ready!')
        animation = Animation (font_size = 72, d=2)
        animation.bind(on_complete=self.fleet.start_attack)
        animation.bind(on_complete=self.shooter.start)
        self.add_widget(label)
        animation.start(label)
    
    def end_game(self,message):
        label=Label(markup=True,size_hint=(.2,.1),pos=(0,self.parent.height/2),text=message)
        self.add_widget(label)
        self.composed_animation().start(label)
    
    def composed_animation(self):
        animation=Animation(center=self.parent.center)
        sound=SoundLoader.load('sounds/go.wav').play()
        animation &= Animation(font_size=72,d=3)
        animation += Animation(font_size=24,y=0,d=2)
        return animation

class InvasionApp(App):
    def build(self):
        return Invasion()

if __name__ in ("__main__"):
    InvasionApp().run()