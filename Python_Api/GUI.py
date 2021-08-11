from typing import Text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    ip = ObjectProperty(None)
    time_I = ObjectProperty(None)
    time_II = ObjectProperty(None)
    time_III = ObjectProperty(None)



    def btn(self):
        print("ip: ", self.ip.text, "time_I: ", self.time_I.text, "time_II: ", self.time_II.text, "time_III: ", self.time_III.text)



class WateringApp(App):

    def build(self):
        return MyGrid()

if __name__ == '__main__':
    WateringApp().run()