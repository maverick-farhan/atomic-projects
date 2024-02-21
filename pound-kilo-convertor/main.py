from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class MainApp(App):
    def build(self):
        self.icon = "scale.png"
        self.convertButton = "Convert to Kilo"
        self.clear = "Clear"

        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color="white",foreground_color="black",
                                  multiline=False,
                                  halign="right",
                                  font_size=55,
                                  readonly=False)

        main_layout.add_widget(self.solution)
        buttons = [
                ["Convert to Kilo"],
                ["Clear"]
                ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                text=label,font_size=30,background_color='black',
                pos_hint={"center_x":.5,"center_y":.5},
                )
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
            button.bind(on_press=self.on_press_action)
        # convert.bind(on_press=self.on_press_convert)
        return main_layout

    def on_press_action(self,instance):
# print("************** Pound to Kilos *******************")
        current = self.solution.text
        button_text = instance.text
        if button_text=='Clear':
            self.solution.text=""
        else:
            pound = self.solution.text
            if pound:
                solution = str((float(pound)*0.453))
                self.solution.text = solution
# print("Weight in Kg: "+ str(kilo))
        

if __name__ == "__main__":
    app = MainApp()
    app.run()
