import random
from threading import Timer
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
        self.score = 0
        self.statusStack = []
        self.prizeMoney = 0
        self.images = ['amzn.png', 'google.png', 'steve.jpg', 'kivy.png', 'trump.png',
                       'lebron.jpg', 'ellen.jpg', 'novak.jpg', 'usain.jpg', 'bill.jpg']*2
        random.shuffle(self.images)
        self.defaulttext = 'Select two values'

    def onClick(self, instance):
        self.instanceText = instance.text
        instance.disabled = True
        instance.background_disabled_normal = './shared/' + \
            self.images[int(instance.text)-1]
        instance.text = ''    
        self.addSelectionToTheStatusStack()
        

    def addSelectionToTheStatusStack(self):
        self.statusStack.append(self.instanceText)
        if(len(self.statusStack) == 2):
            input1 = self.statusStack.pop(-1)
            input2 = self.statusStack.pop(-1)
            if(self.images[int(input1)-1] == self.images[int(input2)-1]):
                print("Yess they got matched")
                self.score += 1
                print("score so far: {0}".format(self.score))
            else:
                print("wrong pair {0} | {1} ".format(input2, input1))
                #some = [input2,input1]
                flipEmOver = Timer(2, self.wrongSelectionFlipEmOver, args=[input2,input1])
                flipEmOver.start()
                #self.wrongSelectionFlipEmOver(input2,input1)    


    def wrongSelectionFlipEmOver(self,*args):
        self.defaulttext = 'Wrong selection try again!'
        #print(self.ids)
        id1 = args[0]
        id2 = args[1]
        self.ids[id1].text = str(id1)
        self.ids[id1].disabled = False
        self.ids[id2].text = str(id2)
        self.ids[id2].disabled = False


class SteveHundreds(App):

    def build(self):
        return SteveHundredsLayout()


calcApp = SteveHundreds()
calcApp.run()
