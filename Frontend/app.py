import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooser
import plyer
from plyer import filechooser
from kivy.storage.jsonstore import JsonStore
from kivy.lang import Builder
from kivy.core.window import Window

class Disc(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        file = filechooser.

        return self.window
    
if __name__ == '__main__':
    Disc().run()