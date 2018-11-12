import random
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.image import Image


# Inherit Kivy's App class which represents the window
# for our widgets
# SteveHundredsLayout inherits all the fields and methods
# from Kivy
# This will also load .kv file and the layout
# in .kv file

class SteveHundredsLayout(GridLayout):
    defaulttext = StringProperty()

    def __init__(self, **kwargs):
        super(SteveHundredsLayout, self).__init__(**kwargs)
        self.count = 0
        self.images=['amzn.png','google.png','steve.jpg','kivy.png','trump.png','lebron.jpg','ellen.jpg','novak.jpg','usain.jpg','bill.jpg']*2
        random.shuffle(self.images)
        self.defaulttext = 'Select two values'

    def onClick(self, instance):
        print(instance.text)
        instance.disabled = True
        instance.background_disabled_normal = './shared/'+self.images[int(instance.text)-1]
        instance.text=''
        self.count += 1
        if(self.count == 2):
            self.count = 0
            print("Here the validation should be happening")
        else:
            self.defaulttext = ''


class SteveHundreds(App):

    def build(self):
        return SteveHundredsLayout()


calcApp = SteveHundreds()
calcApp.run()
