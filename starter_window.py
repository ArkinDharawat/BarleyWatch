from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config

BUTTON_HIT = False
CITY = ""
DATE = ""

class MyApp(App):
# layout
    def build(self):
        self.title = "Barley Watch"
        layout = FloatLayout(size=(500, 500))


        self.lbl1 = Label(text="[color=ff3333][b]Enter City :[/b][/color]",
        markup=True,size_hint=(.2, .05), pos_hint={'x':.3025, 'y':.8})

        layout.add_widget(self.lbl1)

        self.user_text_input = TextInput(text='', multiline=False,
        size_hint=(.2, .05), pos_hint={'x':.5025, 'y':.8})

        layout.add_widget(self.user_text_input)

        self.lbl2 = Label(text="[color=ff3333][b] Enter Crop Date(yyyy/mm/dd): [/b][/color]",
        markup=True,size_hint=(.2, .05), pos_hint={'x':.2025, 'y':.6})

        layout.add_widget(self.lbl2)

        self.user_date_input = TextInput(text='', multiline=False,
        size_hint=(.2, .05), pos_hint={'x':.5025, 'y':.6})

        layout.add_widget(self.user_date_input)

        button = Button(text="OK",size_hint=(.2, .05), pos_hint={'x':.4025, 'y':.5})
        button.bind(on_press=self.buttonClicked)
        layout.add_widget(button)
        return layout

# button click function
    def buttonClicked(self,btn):
        global BUTTON_HIT
        global CITY
        global DATE
        CITY = self.user_text_input.text
        DATE = self.user_date_input.text
        BUTTON_HIT = True
        App.get_running_app().stop()

# run app
def main():
    MyApp().run()
    return BUTTON_HIT,CITY,DATE

 # join all items in a list into 1 big string
