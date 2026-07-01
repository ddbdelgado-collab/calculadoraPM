from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

# --- DISEÑO MEJORADO ---
kv_design = """
<CalculatorWidget>:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    TextInput:
        id: txt_input
        multiline: False
        readonly: True
        halign: "right"
        font_size: 40
        size_hint_y: 0.2
        background_color: (0.1, 0.1, 0.1, 1)
        foreground_color: (1, 1, 1, 1)

    GridLayout:
        cols: 4
        spacing: 5
        
        # Fila 1
        Button:
            text: "7"
            on_press: root.on_button_press(self)
        Button:
            text: "8"
            on_press: root.on_button_press(self)
        Button:
            text: "9"
            on_press: root.on_button_press(self)
        Button:
            text: "/"
            background_color: (0.7, 0.5, 0.2, 1)
            on_press: root.on_button_press(self)

        # Fila 2
        Button:
            text: "4"
            on_press: root.on_button_press(self)
        Button:
            text: "5"
            on_press: root.on_button_press(self)
        Button:
            text: "6"
            on_press: root.on_button_press(self)
        Button:
            text: "*"
            background_color: (0.7, 0.5, 0.2, 1)
            on_press: root.on_button_press(self)

        # Fila 3
        Button:
            text: "1"
            on_press: root.on_button_press(self)
        Button:
            text: "2"
            on_press: root.on_button_press(self)
        Button:
            text: "3"
            on_press: root.on_button_press(self)
        Button:
            text: "-"
            background_color: (0.7, 0.5, 0.2, 1)
            on_press: root.on_button_press(self)

        # Fila 4
        Button:
            text: "."
            on_press: root.on_button_press(self)
        Button:
            text: "0"
            on_press: root.on_button_press(self)
        Button:
            text: "C"
            background_color: (0.8, 0.2, 0.2, 1)
            on_press: root.on_button_press(self)
        Button:
            text: "+"
            background_color: (0.7, 0.5, 0.2, 1)
            on_press: root.on_button_press(self)

    Button:
        text: "="
        size_hint_y: 0.15
        background_color: (0.2, 0.6, 0.2, 1)
        on_press: root.on_solution()
"""

class CalculatorWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.operators = ["+", "-", "*", "/"]
        self.last_was_operator = None

    def on_button_press(self, instance):
        current = self.ids.txt_input.text
        button_text = instance.text

        if button_text == "C":
            self.ids.txt_input.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                self.ids.txt_input.text = current + button_text

        self.last_was_operator = button_text in self.operators

    def on_solution(self):
        text = self.ids.txt_input.text
        if text:
            try:
                solution = str(eval(text))
                self.ids.txt_input.text = solution
            except Exception:
                self.ids.txt_input.text = "Error"

class CalculatorApp(App):
    def build(self):
        Builder.load_string(kv_design)
        return CalculatorWidget()

if __name__ == "__main__":
    CalculatorApp().run()
