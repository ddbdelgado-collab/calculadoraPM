from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window


class CalculadoraApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Blue"
        
        layout_principal = MDBoxLayout(
            orientation='vertical', 
            padding="20dp", 
            spacing="15dp"
        )
        
        self.pantalla = MDTextField(
            text="",
            halign="right",
            font_size="48sp",
            readonly=True,
            mode="rectangle", 
            size_hint_y=None,
            height="100dp"
        )
        layout_principal.add_widget(self.pantalla)
        
        grid_botones = MDGridLayout(
            cols=4, 
            spacing="10dp", 
            size_hint_y=1
        )
        
        botones = [
            'C', '(', ')', '÷',
            '7', '8', '9', 'x',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', 'DEL', '='
        ]
        
        for texto in botones:
            fondo = self.theme_cls.bg_darkest
            texto_color = self.theme_cls.text_color
            
            if texto in ['÷', 'x', '-', '+', '(', ')']:
                fondo = self.theme_cls.primary_color
                texto_color = [1, 1, 1, 1]
                
            elif texto == 'C':
                fondo = self.theme_cls.error_color
                texto_color = [1, 1, 1, 1]
                
            elif texto == '=':
                fondo = self.theme_cls.accent_color
                texto_color = [1, 1, 1, 1]
                
            elif texto == 'DEL':
                fondo = self.theme_cls.primary_dark
                texto_color = [1, 1, 1, 1]

            boton = MDRaisedButton(
                text=texto,
                size_hint=(1, 1),
                font_size="24sp",
                md_bg_color=fondo,
                theme_text_color="Custom",
                text_color=texto_color,
                elevation=2,
                on_release=self.al_presionar_boton
            )
            grid_botones.add_widget(boton)
            
        layout_principal.add_widget(grid_botones)
        return layout_principal

    def al_presionar_boton(self, instancia):
        texto_actual = self.pantalla.text
        texto_boton = instancia.text
        
        if texto_boton == 'C':
            self.pantalla.text = ""
            
        elif texto_boton == 'DEL':
            self.pantalla.text = texto_actual[:-1]
            
        elif texto_boton == '=':
            if texto_actual:
                try:
                    texto_matematico = texto_actual.replace('x', '*').replace('÷', '/')
                    resultado = str(eval(texto_matematico))
                    self.pantalla.text = resultado
                except ZeroDivisionError:
                    self.pantalla.text = "Error: Div/0"
                except Exception:
                    self.pantalla.text = "Error de sintaxis"
                    
        else:
            if "Error" in texto_actual:
                texto_actual = ""
            self.pantalla.text = texto_actual + texto_boton

if __name__ == '__main__':
    CalculadoraApp().run()
