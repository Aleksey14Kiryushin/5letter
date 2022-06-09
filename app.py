# Border у выбранной кнопки
import json
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.base import stopTouchApp

from random import *

# Смена фона
from kivy.core.window import Window

Window.clearcolor = ("#ff99ff")

# Variables
directions = ("right", "left", "down", "up")
words = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
all_objects = list()
position_clicked = 0
counter = 0
all_words = ["арбуз"]
counter_win = 0

result = None
clear = False

# 278 слов


def random_word():
    global the_hidden_word, all_words

    # считываем данные
    with open("data.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        all_words = data["words"]

    print("LEN", len(all_words))
    if len(all_words) != 0:
        the_hidden_word = choice(all_words)
        print(the_hidden_word)
        all_words.remove(the_hidden_word)
        print(all_words)
        print("LEN", len(all_words))

        # Записываем данные
        data = {}
        with open ("data.json", "w", encoding='utf-8') as file:
            data["words"] = all_words
            json.dump(data, file, sort_keys = True)

        return True
        
    return False


class MenuButton(Button):
    def __init__(self, screen, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen

    def on_press(self):
        if responce:
            self.screen.manager.transition.direction = choice(directions)
            self.screen.manager.current = "info" 
        else:
            self.screen.manager.transition.direction = choice(directions)
            self.screen.manager.current = "end" 


class CheckButton(Button):
    def __init__(self, screen, **kwargs):
        super().__init__(**kwargs)

        self.counter = counter
        self.screen = screen

    def on_press(self):
        global counter, the_hidden_word, result, counter_win

        string = ''
        for i in range(5):
            string += all_objects[(counter*5)+i].text
        print(string)

        if "пусто" in string.lower():
            popup = Popup(title='Warning', 
                content=Label(text='Нажмите "Проверить" после того, как введете все буквы в строке'),
                size_hint=(None, None), size=(500,500),
                )
            popup.open()# Показать окно

        else:
            string = string.lower()
            the_hidden_word = the_hidden_word.lower()

            if string == the_hidden_word:
                counter_symbol = 0
                counter_win += 1

                for symbol in string:
                    all_objects[(counter*5)+counter_symbol].background_color = ("#00ff00")
                    counter_symbol += 1

                result = "WIN"

                self.screen.manager.transition.direction = choice(directions)
                self.screen.manager.current = "result" 
                
                print("Вы победили")

            else:
                counter_symbol = 0
                for symbol in string:
                    if not(symbol in the_hidden_word):
                        all_objects[(counter*5)+counter_symbol].background_color = ("#ff0000")
                        print(f"{symbol} - 1")

                    elif symbol in the_hidden_word and string.find(symbol) == the_hidden_word.find(symbol):
                        all_objects[(counter*5)+counter_symbol].background_color = ("#00ff00")
                        print(f"{symbol} - 2")

                    elif symbol in the_hidden_word and string.find(symbol) != the_hidden_word.find(symbol):
                        all_objects[(counter*5)+counter_symbol].background_color = ("#0066ff")
                        print(f"{symbol} - 3")

                    counter_symbol += 1

                

                print("Попытка израсходована")
            counter += 1
            print("COUNTER", counter)

            if counter == 5:
                result = "DEFEAT"

                self.screen.manager.transition.direction = choice(directions)
                self.screen.manager.current = "result"


class ButtonAlphabet(Button):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text

    def on_press(self):
        all_objects[position_clicked].text = self.text
        print("THE WORD IS", self.text)
        

class ButtonCell(Button):
    def __init__(self, text, position_x, position_y, **kwargs):
        global all_objects
        super().__init__(**kwargs)
        self.text = text
        self.position = position_x + position_y*5 
        
        all_objects.append(self)

    def on_press(self):
        global position_clicked
        
        # self.border = (10,10,10,10)

        position_clicked = self.position

        print("THE POSITION IS", self.position)

    

class InfoScr(Screen):
    def __init__(self, name="info"): 
        super().__init__(name=name)

        lbl = Button(text="5Words",
                    color=("#000000"),
                     disabled=True,
                     size_hint=(.5,.2),
                )

        instruction = Label(text="Что означают цвета букв после Проверки:\n\n· Зеленый - буква расположена в загаданном слове в том же месте, что и введена;\n\n· Синий - введенная буква присутствует в слове, но не соответствует расположению в загаданном;\n\n· Красный - буква не присутсвует в загаданном слове.")

        self.btn_begin = Button(
            text="Начать",
            size_hint=(1,.5),
            background_color="#ff4dc4"
        )

        self.btn_begin.on_press = self.next

        layout_horiz = BoxLayout(orientation="vertical", spacing=10, padding=4)

        layout_horiz.add_widget(lbl)
        layout_horiz.add_widget(instruction)
        layout_horiz.add_widget(self.btn_begin)

        self.add_widget(layout_horiz)

    def next(self):
        self.manager.transition.direction = choice(directions)
        self.manager.current = "gaming" 

class GameScr(Screen):
    def __init__(self, name="gaming"):     
        super().__init__(name=name)
        lbl = Button(text="5Words",
                    color=("#000000"),
                    disabled=True,
                    #  size_hint=(.2,.1),            
                )

        # # кнопки
        self.layout_all = BoxLayout(orientation="vertical")
        for i in range(5):
            layout_vert = BoxLayout(orientation="horizontal")
            for step in range(5):
                word = ButtonCell(text="Пусто", 
                    position_x=step, position_y=i,
                    background_color=("#66ffff")
                )
                layout_vert.add_widget(word)
            self.layout_all.add_widget(layout_vert)

        # клавиатура
        self.layout_all_qwwery = BoxLayout(orientation="vertical")
        for i in range(3):
            layout_vert_qwerty = BoxLayout(orientation="horizontal")
            for symbol in range(11):
                word = ButtonAlphabet(text=str(words[(i*11)+(symbol)]),
                                    background_color =("#cc3399"))
                layout_vert_qwerty.add_widget(word)

            self.layout_all_qwwery.add_widget(layout_vert_qwerty) 

        # Menu
        check_btn = CheckButton(self, text="Проверить",
                        # size_hint=(.2,.1)
                        background_color=("#00ff00")  
                        )

        menu_btn = MenuButton(self, text="Меню",
                        background_color=("#0000b3")
                        # size_hint=(.2,.1)
                        )

        # layouts
        self.layout_horiz = BoxLayout(orientation="vertical", spacing=10)
        
        self.layout_menu = BoxLayout(orientation="horizontal", 
                                spacing=2, size_hint=(1,.5))

        self.layout_menu.add_widget(lbl)
        self.layout_menu.add_widget(menu_btn)
        self.layout_menu.add_widget(check_btn)

        self.layout_horiz.add_widget(self.layout_menu)
        self.layout_horiz.add_widget(self.layout_all)
        self.layout_horiz.add_widget(self.layout_all_qwwery)

        self.add_widget(self.layout_horiz)

    def on_enter(self):
        global all_objects, clear
        if clear:
            print("ПЕРЕХОД")
            self.layout_all.clear_widgets()
            self.layout_horiz.clear_widgets()

        # очищаем список форм, чтобы избежать ошибку, когда не видим букв
            all_objects = list()


            for i in range(5):
                layout_vert = BoxLayout(orientation="horizontal")
                for step in range(5):
                    word = ButtonCell(text="Пусто", 
                        position_x=step, position_y=i,
                        background_color=("#66ffff")
                    )
                    layout_vert.add_widget(word)
                self.layout_all.add_widget(layout_vert)

            self.layout_horiz.add_widget(self.layout_menu)
            self.layout_horiz.add_widget(self.layout_all)
            self.layout_horiz.add_widget(self.layout_all_qwwery)

            clear = False
        

class ResultScr(Screen):
    def __init__(self, name="result"): 
        super().__init__(name=name)

        self.result_lbl = Label(text="Поздравляем, Вы победили!")

        self.menu = MenuButton(self, text="Перейти в главное меню")

        self.lbl_passed = Label(text="Пройдено ...")

        layout = BoxLayout(orientation="vertical")

        layout.add_widget(self.result_lbl)
        layout.add_widget(self.lbl_passed)
        layout.add_widget(self.menu)

        self.add_widget(layout)

    def on_enter(self):
        global result, the_hidden_word, counter, position_clicked, clear, responce

        if result == "DEFEAT":
            self.result_lbl.text = f"К сожалению, вы проиграли!\nМы загадали слово: {the_hidden_word}..."

        self.lbl_passed.text = f"Пройдено {278 - len(all_words)} из 278 слов"

        counter = 0
        position_clicked = 0
        result = None
        clear = True
        responce = random_word()

class EndScr(Screen):
    def __init__(self, name="end"): 
        super().__init__(name=name)

        self.lbl = Label(text="Поздравдяем, Вы прошли игру!\nСтатистика: Вы угадали ... слов из 278\nЖдите обновлений и последующих версий...")

        self.add_widget(self.lbl)

    def on_enter(self):
        self.lbl.text = f"Поздравдяем, Вы прошли игру!\nСтатистика: Вы угадали {counter_win} из 278 слов\nЖдите обновлений и последующих версий..."

class Game(App):
    def build(self):
    
        scr_manager = ScreenManager()
        # ДОбавление экранов
        scr_manager.add_widget(InfoScr(name="info"))

        scr_manager.add_widget(GameScr(name="gaming"))

        scr_manager.add_widget(ResultScr(name="result"))

        scr_manager.add_widget(EndScr(name="end"))

        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        scr_manager.current = "info"

        return scr_manager

# Вызывается единожды
responce = random_word()

app = Game()
app.run()
