import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.app import App
from kivy.uix.button import Button
 

# Inherit Kivy's App class which represents the window
# for our widgets
# SteveHundredsLayout inherits all the fields and methods
# from Kivy
#This will also load .kv file and the layout
#in .kv file

class SteveHundredsLayout(GridLayout):
    pass    
 
class SteveHundreds(App):
 
    def build(self):
        return SteveHundredsLayout()
 
calcApp = SteveHundreds()
calcApp.run()