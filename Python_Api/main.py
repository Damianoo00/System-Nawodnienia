from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class ConnectWindow(Screen):
    #ip = ObjectProperty(None)

    def ConnectWithPLC(self):
        return True

class MainWindow(Screen):
    pass


class SetWindow(Screen):
    time_I = ObjectProperty(None)
    time_II = ObjectProperty(None)
    time_III = ObjectProperty(None)



    def btn(self):
        #print("ip: ", self.ip.text, "time_I: ", self.time_I.text, "time_II: ", self.time_II.text, "time_III: ", self.time_III.text)
        pass
class TestWindow(Screen):
    
    def change_color(self):
        pass

class ProcessWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("watering.kv")





class WateringMainApp(App):

    def build(self):
        return kv
if __name__ == '__main__':
    WateringMainApp().run()