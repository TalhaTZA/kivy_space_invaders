from kivy.uix.image import Image
from kivy.core.audio import SoundLoader


class Boom(Image):
    sound=SoundLoader.load('sounds/boom.wav')
    
    def __init__(self,**kwargs):
        self.__class__.sound.play()
        super().__init__(**kwargs)