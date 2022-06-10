# Border у выбранной кнопки
import json
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup


from random import *

# Смена фона
from kivy.core.window import Window

Window.clearcolor = ("#ff99ff")

# Variables
directions = ("right", "left", "down", "up")
words = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

all_objects = list()
keyboard_objects = list()

position_clicked = 0
counter = 0
counter_win = 0

result = None
clear = False

# 278 слов
all_words = ["\u0430\u0431\u0437\u0430\u0446", "\u0430\u043a\u0430\u0442\u044c", "\u0430\u043c\u0431\u0430\u0440", "\u0430\u0440\u0433\u043e\u043d", "\u0430\u0442\u043b\u0435\u0442", "\u0430\u0432\u043e\u0441\u044c", "\u0430\u043a\u0446\u0438\u044f", "\u0430\u043c\u043f\u0438\u0440", "\u0430\u0440\u043c\u0438\u044f", "\u0430\u0433\u0435\u043d\u0442", "\u0431\u0430\u043b\u043a\u0430", "\u0431\u0430\u0440\u043e\u043d", "\u0431\u0435\u0433\u043e\u043c", "\u0431\u0438\u0432\u043d\u0438", "\u0431\u043b\u0430\u043d\u043a", "\u0431\u043e\u043b\u0438\u0434", "\u0431\u0440\u0430\u0441\u0441", "\u0431\u0443\u0434\u043d\u0438", "\u0431\u0443\u0440\u0443\u043d", "\u0431\u0430\u0431\u043a\u0430", "\u0432\u0437\u0434\u043e\u0445", "\u0432\u0438\u0442\u0438\u044f", "\u0432\u043d\u0438\u0437\u0443", "\u0432\u043e\u0437\u043e\u043a", "\u0432\u043e\u0442\u0449\u0435", "\u0432\u0441\u044e\u0434\u0443", "\u0432\u044b\u0432\u043e\u0437", "\u0432\u044b\u0448\u043a\u0430", "\u0432\u0430\u0437\u043e\u043d", "\u0432\u0430\u044f\u0442\u044c", "\u0433\u0430\u0440\u0443\u0441", "\u0433\u043b\u0430\u0432\u043a", "\u0433\u043e\u043b\u0435\u0446", "\u0433\u043e\u0440\u043e\u0434", "\u0433\u0440\u043e\u0441\u0441", "\u0433\u0443\u0440\u0438\u044f", "\u0433\u0430\u0437\u0438\u043a", "\u0433\u0435\u043d\u0438\u0439", "\u0433\u043b\u0443\u0448\u044c", "\u0433\u043e\u043b\u044b\u0448", "\u0434\u0435\u0431\u043e\u0448", "\u0434\u0435\u0442\u043a\u0430", "\u0434\u043e\u0433\u043c\u0430", "\u0434\u043e\u0441\u044b\u043b", "\u0434\u0440\u043e\u0432\u0430", "\u0434\u0443\u0442\u044b\u0439", "\u0434\u0435\u0438\u0437\u043c", "\u0434\u0438\u043a\u0438\u0439", "\u0434\u043e\u043a\u0435\u0440", "\u0434\u0440\u0430\u0433\u0430", "\u0435\u0432\u0440\u0435\u0438", "\u0435\u0437\u0434\u043a\u0430", "\u0435\u0440\u0435\u0441\u044c", "\u0435\u0432\u043d\u0443\u0445", "\u0435\u0436\u0438\u0445\u0430", "\u0435\u043c\u043a\u0438\u0439", "\u0435\u0436\u0435\u043b\u0438", "\u0435\u043a\u0430\u0442\u044c", "\u0435\u0434\u043a\u0438\u0439", "\u0435\u0437\u0436\u0430\u0439", "\u0436\u0430\u043a\u0435\u0442", "\u0436\u0438\u0432\u043e\u0439", "\u0436\u0443\u043f\u0435\u043b", "\u0436\u0432\u0430\u043b\u0430", "\u0436\u0438\u043b\u043a\u0430", "\u0436\u0435\u0440\u0434\u044c", "\u0436\u0438\u0442\u044c\u0435", "\u0436\u0430\u043a\u0430\u043d", "\u0436\u0438\u0432\u0435\u0446", "\u0436\u0443\u043f\u0430\u043d", "\u0437\u0430\u0434\u043e\u043c", "\u0437\u0430\u043b\u043e\u0433", "\u0437\u0430\u0440\u044f\u0434", "\u0437\u0432\u0435\u0440\u044c", "\u0437\u043b\u044e\u043a\u0430", "\u0437\u0430\u0431\u043e\u0440", "\u0437\u0430\u0437\u043e\u0440", "\u0437\u0430\u043d\u043e\u0441", "\u0437\u0430\u0442\u0435\u044f", "\u0437\u0435\u043c\u043b\u044f", "\u0438\u0434\u0438\u043e\u0442", "\u0438\u043a\u043e\u043d\u0430", "\u0438\u0441\u0442\u044b\u0439", "\u0438\u0437\u0432\u043d\u0435", "\u0438\u043d\u0436\u0438\u0440", "\u0438\u0448\u0438\u0430\u0441", "\u0438\u0432\u0430\u0441\u0438", "\u0438\u0437\u043b\u0435\u0442", "\u0438\u0441\u043a\u0440\u0430", "\u0438\u0434\u0435\u0430\u043b", "\u043a\u043e\u043c\u043e\u0434", "\u043a\u043e\u0440\u043a\u0430", "\u043a\u043e\u0448\u043a\u0430", "\u043a\u0440\u043e\u0441\u0441", "\u043a\u0443\u043a\u043b\u0430", "\u043a\u0443\u043f\u043e\u043d", "\u043a\u0430\u0437\u043d\u044c", "\u043a\u0430\u043d\u0430\u043b", "\u043a\u0430\u0441\u043a\u0430", "\u043a\u0432\u043e\u0442\u0430", "\u043b\u0430\u0432\u0430\u0448", "\u043b\u0430\u0442\u043a\u0430", "\u043b\u0435\u043c\u0443\u0440", "\u043b\u0438\u043a\u0435\u0440", "\u043b\u0438\u0448\u0430\u0439", "\u043b\u0443\u0431\u043e\u043a", "\u043b\u044f\u0436\u043a\u0430", "\u043b\u0430\u0437\u0435\u0440", "\u043b\u0435\u0432\u0430\u043a", "\u043b\u0435\u043f\u0442\u0430", "\u043c\u044f\u043a\u0438\u0448", "\u043c\u0430\u043a\u0430\u0440", "\u043c\u0430\u043d\u043e\u043a", "\u043c\u0430\u0447\u0442\u0430", "\u043c\u0435\u0442\u043a\u0430", "\u043c\u0438\u0442\u0440\u0430", "\u043c\u043e\u0440\u043e\u0437", "\u043c\u0443\u043b\u043b\u0430", "\u043c\u0430\u0433\u0438\u044f", "\u043c\u0430\u043b\u044b\u0439", "\u043d\u0430\u0433\u0430\u043d", "\u043d\u0430\u043b\u0435\u0442", "\u043d\u0430\u0440\u044f\u0434", "\u043d\u0435\u043a\u0438\u0439", "\u043d\u0438\u043a\u0430\u043a", "\u043d\u043e\u0441\u0438\u043a", "\u043d\u0430\u0431\u0430\u0442", "\u043d\u0430\u0434\u043e\u0439", "\u043d\u0430\u043c\u0435\u043a", "\u043d\u0430\u0446\u0438\u044f", "\u043e\u0431\u0438\u0434\u0430", "\u043e\u0431\u0443\u0437\u0430", "\u043e\u0436\u0435\u0447\u044c", "\u043e\u043a\u0441\u0438\u0434", "\u043e\u043f\u0430\u043b\u0430", "\u043e\u0440\u0430\u043b\u043e", "\u043e\u0441\u043e\u0431\u044c", "\u043e\u0442\u0434\u0435\u043b", "\u043e\u0442\u0440\u044f\u0434", "\u043e\u0447\u0435\u0440\u043a", "\u043f\u0435\u0447\u043a\u0430", "\u043f\u0438\u0441\u0435\u0446", "\u043f\u043b\u0435\u0447\u043e", "\u043f\u043e\u0436\u043d\u044f", "\u043f\u043e\u043b\u0431\u0430", "\u043f\u043e\u043c\u043e\u0440", "\u043f\u043e\u0441\u0430\u0434", "\u043f\u043e\u0447\u043a\u0430", "\u043f\u0440\u0438\u044e\u0442", "\u043f\u0443\u043b\u044c\u0441", "\u0440\u0430\u0437\u0432\u0435", "\u0440\u0430\u0445\u0438\u0442", "\u0440\u0435\u0437\u043a\u0430", "\u0440\u0438\u0444\u043c\u0430", "\u0440\u043e\u043b\u0438\u043a", "\u0440\u0443\u0438\u043d\u0430", "\u0440\u044b\u043d\u0434\u0430", "\u0440\u0430\u043b\u043b\u0438", "\u0440\u0432\u0430\u0442\u044c", "\u0440\u0435\u043b\u044c\u0441", "\u0441\u0430\u043d\u043a\u0438", "\u0441\u0432\u0430\u0445\u0430", "\u0441\u0434\u0443\u0442\u044c", "\u0441\u0435\u0440\u0438\u044f", "\u0441\u0438\u0437\u044b\u0439", "\u0441\u043a\u0430\u043b\u0430", "\u0441\u043b\u0430\u0432\u0430", "\u0441\u043c\u0435\u043d\u0430", "\u0441\u043d\u043e\u0432\u0430", "\u0441\u043e\u043f\u043a\u0430", "\u0442\u043e\u043b\u043a\u0438", "\u0442\u043e\u0449\u0438\u0439", "\u0442\u0440\u043e\u043f\u0430", "\u0442\u0443\u0440\u043a\u0430", "\u0442\u044f\u043f\u043a\u0430", "\u0442\u0430\u0431\u0443\u043d", "\u0442\u0430\u043d\u0435\u0446", "\u0442\u0435\u0438\u0437\u043c", "\u0442\u0435\u0447\u043a\u0430", "\u0442\u0438\u0440\u0430\u043d", "\u0443\u0437\u043a\u0438\u0439", "\u0443\u043d\u0446\u0438\u044f", "\u0443\u0442\u0438\u0446\u0430", "\u0443\u0432\u0438\u0442\u044c", "\u0443\u043a\u0440\u043e\u043f", "\u0443\u0441\u0435\u0447\u044c", "\u0443\u0447\u0435\u0431\u0430", "\u0443\u0434\u0438\u043b\u0430", "\u0443\u043c\u0435\u0442\u044c", "\u0443\u0441\u0442\u0443\u043f", "\u0444\u0430\u0437\u0430\u043d", "\u0444\u0435\u0441\u043a\u0430", "\u0444\u0438\u043d\u043d\u044b", "\u0444\u0440\u0430\u043d\u043a", "\u0444\u0430\u043b\u044c\u0446", "\u0444\u0438\u0437\u0438\u043a", "\u0444\u043b\u0435\u0448\u044c", "\u0444\u0440\u043e\u043d\u0442", "\u0444\u0430\u0443\u043d\u0430", "\u0444\u0438\u043b\u043e\u043d", "\u0445\u0430\u0439\u043b\u043e", "\u0445\u0438\u043c\u0438\u044f", "\u0445\u043e\u043b\u043e\u043f", "\u0445\u0443\u0440\u0430\u043b", "\u0445\u0430\u043c\u0441\u0430", "\u0445\u043b\u044b\u0441\u0442", "\u0445\u043e\u0440\u0430\u043b", "\u0445\u0432\u043e\u0440\u044c", "\u0445\u043e\u0431\u043e\u0442", "\u0445\u043e\u0445\u043c\u0430", "\u0446\u0438\u0442\u0440\u0430", "\u0446\u0432\u0435\u0442\u043e", "\u0446\u044b\u043f\u043a\u0430", "\u0446\u0435\u043d\u0442\u0440", "\u0446\u0438\u043d\u0438\u043a", "\u0446\u0430\u043f\u043b\u044f", "\u0446\u0443\u0446\u0438\u043a", "\u0446\u0435\u043b\u044b\u0439", "\u0446\u0438\u043d\u0433\u0430", "\u0446\u0430\u043f\u043a\u0430", "\u0447\u0443\u0434\u0438\u043a", "\u0447\u0430\u044f\u0442\u044c", "\u0447\u0435\u0448\u0443\u044f", "\u0447\u0443\u043a\u0447\u0438", "\u0447\u0435\u0440\u0432\u044c", "\u0447\u0438\u0441\u043b\u043e", "\u0447\u0440\u0435\u0437\u043e", "\u0447\u0443\u0440\u043a\u0430", "\u0447\u0430\u043b\u043c\u0430", "\u0447\u0435\u0440\u0442\u0430", "\u0448\u0430\u0432\u043a\u0430", "\u0448\u0430\u0442\u0435\u043d", "\u0448\u0435\u0440\u0438\u0444", "\u0448\u043a\u043e\u0434\u0430", "\u0448\u043f\u0430\u0442\u044b", "\u0448\u0442\u0443\u043a\u0430", "\u0448\u0430\u043b\u0430\u0448", "\u0448\u0430\u0445\u0442\u0430", "\u0448\u0438\u043f\u0443\u043d", "\u0449\u0435\u043f\u043a\u0430", "\u0449\u0438\u0442\u043e\u043a", "\u0449\u0435\u043d\u043e\u043a", "\u0449\u0438\u043f\u0446\u044b", "\u0449\u0435\u043b\u043e\u043a", "\u0449\u0438\u043f\u043e\u043a", "\u0449\u0435\u043b\u043a\u0430", "\u0449\u0435\u0447\u043a\u0430", "\u0449\u0435\u043a\u043e\u0442", "\u0449\u0435\u0442\u043a\u0430", "\u044d\u0441\u043a\u0438\u0437", "\u044d\u043b\u0438\u0442\u0430", "\u044d\u0440\u043a\u0435\u0440", "\u044d\u043a\u0440\u0430\u043d", "\u044d\u0440\u0437\u0430\u0446", "\u044d\u0442\u043d\u043e\u0441", "\u044d\u043a\u043b\u0435\u0440", "\u044d\u043f\u043e\u0445\u0430", "\u044d\u0442\u0438\u043a\u0430", "\u044d\u0432\u0435\u043d\u044b", "\u044e\u043a\u043e\u043b\u0430", "\u044e\u043d\u043e\u0448\u0430", "\u044e\u0434\u043e\u043b\u044c", "\u044e\u043d\u043d\u0430\u0442", "\u044e\u043d\u043a\u0435\u0440", "\u044e\u043d\u0438\u043e\u0440", "\u044e\u0440\u043a\u0438\u0439", "\u044e\u043b\u0438\u0442\u044c", "\u044e\u0440\u0438\u0441\u0442", "\u044f\u0433\u0435\u043b\u044c", "\u044f\u0445\u043e\u043d\u0442", "\u044f\u043a\u043e\u0440\u044c", "\u044f\u0440\u043b\u044b\u043a", "\u044f\u0432\u043d\u044b\u0439", "\u044f\u0441\u0442\u044b\u043a", "\u044f\u043a\u043e\u0431\u044b", "\u044f\u0440\u043a\u0438\u0439", "\u044f\u0432\u0438\u0442\u044c", "\u044f\u0441\u0442\u0432\u043e"]

def active_btn(position_clicked):
    for i in range(counter*5,len(all_objects)):
        all_objects[i].background_color = "#66ffff"

    all_objects[position_clicked].background_color = (255, 255, 0, .7)

def random_word():
    global the_hidden_word, all_words
    
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
                clear_string = the_hidden_word
                player_string = string

                counter_symbol = 0
                # for symbol in string:
                #     if not(symbol in the_hidden_word):
                #         all_objects[(counter*5)+counter_symbol].background_color = ("#ff0000")
                #         print(f"{symbol} - 1")

                #     elif symbol in the_hidden_word and string.find(symbol) != the_hidden_word.find(symbol):
                #         all_objects[(counter*5)+counter_symbol].background_color = ("#0066ff")
                #         print("SYMBOL 2", symbol)
                #         print(f"{symbol} - 3")

                #     elif symbol in the_hidden_word and string.find(symbol) == the_hidden_word.find(symbol):
                #         all_objects[(counter*5)+counter_symbol].background_color = ("#00ff00")
                #         print("SYMBOL 3", symbol)
                #         print(f"{string.find(symbol)} - {string}")
                #         print(f"{symbol} - 2")
                
                for symbol in string:
                    if not(symbol in the_hidden_word):
                        all_objects[(counter*5)+counter_symbol].background_color = ("#ff0000")
                        print(f"{symbol} - 1")
                        # print(f"{symbol} - {words.lower().find(symbol)} - {keyboard_objects[words.lower().find(symbol)].text()}")

                        keyboard_objects[words.lower().find(symbol)].background_color = ("#ff0000")

                    else:
                        all_objects[(counter*5)+counter_symbol].background_color = ("#0066ff")

                        keyboard_objects[words.lower().find(symbol)].background_color = ("#0066ff")

                        if player_string.find(symbol) + counter_symbol == clear_string.find(symbol) + counter_symbol:
                            all_objects[(counter*5)+counter_symbol].background_color = ("#00ff00")
                            
                            keyboard_objects[words.lower().find(symbol)].background_color = ("#00ff00")


                    # elif symbol in the_hidden_word and player_string.find(symbol) + counter_symbol != clear_string.find(symbol) + counter_symbol:
                    #     all_objects[(counter*5)+counter_symbol].background_color = ("#0066ff")
                    #     print("SYMBOL 2", symbol)
                    #     print(f"{symbol} - 3")

                    #     # keyboard_objects[words.find(symbol.upper())].background_color = ("#0066ff")


                    # elif symbol in the_hidden_word and player_string.find(symbol) + counter_symbol == clear_string.find(symbol) + counter_symbol:
                    #     all_objects[(counter*5)+counter_symbol].background_color = ("#00ff00")
                    #     print("SYMBOL 3", symbol)
                    #     print(f"{string.find(symbol)} - {string}")
                    #     print(f"{symbol} - 2")

                    #     print(f"Word - {symbol} - {words.find(symbol)} - {keyboard_objects[words.find(symbol)]}")
                    #     # keyboard_objects[words.find(symbol.upper())].background_color = ("#00ff00")


                    counter_symbol += 1
                    clear_string = the_hidden_word[counter_symbol : 5]
                    player_string = string[counter_symbol : 5]

                    print("clear_string", clear_string)
                    print("player_string", player_string)

            if counter == 4 and string != the_hidden_word:
                result = "DEFEAT"

                self.screen.manager.transition.direction = choice(directions)
                self.screen.manager.current = "result"
          
            counter += 1
            print("COUNTER", counter)
            print("Попытка израсходована")


class ButtonAlphabet(Button):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text

        keyboard_objects.append(self)
    def on_press(self):
        global position_clicked, keyboard_objects

        if position_clicked >= counter*5 and position_clicked < (counter+1)*5:
            all_objects[position_clicked].text = self.text

            # на следующую
            print("Position Before:", position_clicked)
            position_clicked += 1
            print("Position After:", position_clicked)

            print("THE WORD IS", self.text)

            # меняем цвет
            if position_clicked >= counter*5 and position_clicked + 1 <= (counter+1)*5:
                active_btn(position_clicked)
            else:
                position_clicked -= 1
        

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

        # меняем цвет
        if position_clicked >= counter*5 and position_clicked < (counter+1)*5:
            active_btn(position_clicked)

class InfoScr(Screen):
    def __init__(self, name="info"): 
        super().__init__(name=name)

        lbl = Button(text="5Words",
                    color=("#000000"),
                     disabled=True,
                     size_hint=(.5,.2),
                )

        instruction = Label(text="Что означают цвета букв после Проверки:\n\n· Зеленый - буква расположена в загаданном слове в том же\nместе, что и введена;\n\n· Синий - введенная буква присутствует в слове,\n но не соответствует расположению в загаданном;\n\n· Красный - буква не присутсвует в загаданном слове.",halign= 'center')

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
        global all_objects, clear, keyboard_objects
        if clear:
            print("ПЕРЕХОД")
            self.layout_all.clear_widgets()
            self.layout_horiz.clear_widgets()
            self.layout_all_qwwery.clear_widgets()

        # очищаем список форм, чтобы избежать ошибку, когда не видим букв
            all_objects = list()
            keyboard_objects = list()

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
            for i in range(3):
                layout_vert_qwerty = BoxLayout(orientation="horizontal")
                for symbol in range(11):
                    word = ButtonAlphabet(text=str(words[(i*11)+(symbol)]),
                                        background_color =("#cc3399"))
                    layout_vert_qwerty.add_widget(word)

                self.layout_all_qwwery.add_widget(layout_vert_qwerty) 


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
