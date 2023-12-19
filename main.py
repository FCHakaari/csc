from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window

class Main_app(App):
    def build(self):
        return Frontend()

class ClearTextInput(TextInput):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.text=''
        return super().on_touch_down(touch)
    
class Frontend(GridLayout):  
    def __init__(self, **kwargs):
        super(Frontend, self).__init__(**kwargs)
        self.cols = 1

        self.text_1, self.itog, self.result=0,0,0
     
        self.main_fn()
    
    def filter_digits(self, text, from_undo, *args):
        return ''.join([c for c in text if c.isdigit()])
    
    def main_fn(self):

        self.sum=ClearTextInput(hint_text='Введите необходимую сумму', multiline=False, input_filter=self.filter_digits)
        self.ostatok=ClearTextInput(hint_text='Остаток в кассе(стандартно 1500)', multiline=False, input_filter=self.filter_digits)
        self.one_ru=ClearTextInput(hint_text='Введите кол-во рублей', multiline=False, input_filter=self.filter_digits)
        self.two_ru=ClearTextInput(hint_text='Введите кол-во двоек', multiline=False, input_filter=self.filter_digits)
        self.five_iron_ru=ClearTextInput(hint_text='Введите кол-во железных пятерок', multiline=False, input_filter=self.filter_digits)
        self.five_paper_ru=ClearTextInput(hint_text='Введите кол-во бумажных пятерок', multiline=False, input_filter=self.filter_digits)
        self.ten_iron_ru=ClearTextInput(hint_text='Введите кол-во железных десяток', multiline=False, input_filter=self.filter_digits)
        self.ten_paper_ru=ClearTextInput(hint_text='Введите кол-во бумажных десяток', multiline=False, input_filter=self.filter_digits)
        self.fifty_ru=ClearTextInput(hint_text='Введите кол-во пятидесяток', multiline=False, input_filter=self.filter_digits)
        self.hundred_ru=ClearTextInput(hint_text='Введите кол-во соток', multiline=False, input_filter=self.filter_digits)
        self.two_hundred_ru=ClearTextInput(hint_text='Введите кол-во двухсоток', multiline=False, input_filter=self.filter_digits)
        self.five_hundred_ru=ClearTextInput(hint_text='Введите кол-во пятисоток ', multiline=False, input_filter=self.filter_digits)
        self.thousand_ru=ClearTextInput(hint_text='Введите кол-во тысяч', multiline=False, input_filter=self.filter_digits)
        self.two_thousand_ru=ClearTextInput(hint_text='Введите кол-во двухтысячных', multiline=False, input_filter=self.filter_digits)
        self.five_thousand_ru=ClearTextInput(hint_text='Введите кол-во пятитысячных', multiline=False, input_filter=self.filter_digits)
        
        self.clear_text_input=Button(text='Очистить поля')
        self.activity_button=Button(text='Выполнить вычисления ')

        self.vsego=Label(text=str(self.result))
        self.itog=Label(text=str(self.text_1))
        self.ostatok.text='1500'

        def reset_wid(ros):
            self.sum.text = 'Введите необходимую сумму'
            self.ostatok.text='1500'
            self.one_ru.text = 'Введите сумму рублей'
            self.two_ru.text = 'Введите сумму двоек'
            self.five_iron_ru.text = 'Введите сумму железных пятерок'
            self.five_paper_ru.text = 'Введите сумму бумажных пятерок'
            self.ten_iron_ru.text = 'Введите сумму железных десяток'
            self.ten_paper_ru.text = 'Введите сумму бумажных десяток'
            self.hundred_ru.text='Введите сумму соток'
            self.fifty_ru.text = 'Введите сумму пятидесяток'
            self.hundred_ru.text = 'Введите сумму соток'
            self.two_hundred_ru.text = 'Введите сумму двухсоток'
            self.five_hundred_ru.text = 'Введите сумму пятисоток'
            self.thousand_ru.text = 'Введите сумму тысяч'
            self.two_thousand_ru.text = 'Введите сумму двухтысячных'
            self.five_thousand_ru.text = 'Введите сумму пятитысячных'

        def sum_fn(tos):     

            s=[self.sum ,self.one_ru, self.two_ru, self.five_iron_ru, self.five_paper_ru, self.ten_iron_ru, self.ten_paper_ru, self.fifty_ru, self.hundred_ru, self.two_hundred_ru, self.five_hundred_ru, self.thousand_ru, self.two_thousand_ru, self.five_thousand_ru]
            for i in s:
                if not i.text.isdigit():
                    i.text = '0'

            result=int(self.one_ru.text) + int(self.two_ru.text) + int(self.five_iron_ru.text) + int(self.five_paper_ru.text) + int(self.ten_iron_ru.text) + int(self.ten_paper_ru.text) + int(self.fifty_ru.text) + int(self.two_hundred_ru.text) + int(self.five_hundred_ru.text) + int(self.thousand_ru.text) + int(self.two_thousand_ru.text) + int(self.five_thousand_ru.text)
            
            ss=(int(self.sum.text)-int(self.ostatok.text)-result)
            if int(self.sum.text)<result:
                self.text_1='У Вас больше на '+str(abs(ss))
            elif int(self.sum.text)>result:
                self.text_1='У Вас не хватает: '+str(abs(ss))
            elif int(self.sum.text)==result:
                self.text_1='У Вас все идеально' 
            res=result+int(self.ostatok.text)
            sd='В кассе(без размена): '+str(result)+' | (с разменом) ' +str(res)

            self.vsego.text=str(sd)
            self.itog.text=str(self.text_1)
        
        self.clear_text_input.bind(on_press=reset_wid)
        self.activity_button.bind(on_press=sum_fn)

        self.add_widget(self.sum)
        self.add_widget(self.ostatok)
        self.add_widget(self.one_ru)
        self.add_widget(self.two_ru)
        self.add_widget(self.five_iron_ru)
        self.add_widget(self.five_paper_ru)
        self.add_widget(self.ten_iron_ru)
        self.add_widget(self.ten_paper_ru)
        self.add_widget(self.fifty_ru)
        self.add_widget(self.hundred_ru)
        self.add_widget(self.two_hundred_ru)
        self.add_widget(self.five_hundred_ru)
        self.add_widget(self.thousand_ru)
        self.add_widget(self.two_thousand_ru)
        self.add_widget(self.five_thousand_ru)
        self.add_widget(self.clear_text_input)
        self.add_widget(self.activity_button)
        self.add_widget(self.vsego)
        self.add_widget(self.itog)

if __name__ == '__main__':
    Main_app().run()    
