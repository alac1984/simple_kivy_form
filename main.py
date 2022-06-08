from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget, ObjectProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen

data = {}

class MainWindow(Screen):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    city = ObjectProperty(None)
    country = ObjectProperty(None)

    def first_press(self):
        data['fname'] = self.fname.text
        data['lname'] = self.lname.text
        data['city'] = self.city.text
        data['country'] = self.country.text

        print(data)


class SecondWindow(Screen):
    interests = ObjectProperty(None)
    contact = ObjectProperty(None)

    def second_press(self):
        data['interests'] = self.interests.text
        data['contact'] = self.contact.text

        print(data)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('kivyform.kv')


class KivyFormApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    KivyFormApp().run()
