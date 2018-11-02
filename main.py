import sqlite3

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen




key = 1


class MenuScreen(Screen):
    pass


class Next(Screen):
    pass


def entarabartion(string, key):
    encript_string = ''
    for letter in string:
        encript_string += chr(ord(letter) ^ key)
    return encript_string


def detarabartion(string, key):
    return entarabartion(string, key)


def checkSQL(user, password):
    try:
        connect = sqlite3.connect("mydatabase.db")
    except:
        pass
    cursor = connect.cursor()

    text = "SELECT * FROM table1 WHERE user = '"+user+"'"

    cursor.execute(text)
    results = cursor.fetchone()

    connect.commit()
    connect.close()

    return results


class MyApp(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', size_hint=[.5, .35])

        self.w1 = TextInput(text='Пользователь', font_size=30, multiline=False)
        self.w2 = TextInput(text='Пароль', font_size=30, password=True, multiline=False)
        self.w3 = Button(text='Войти', on_press=self.btn_press)

        bl.add_widget(self.w1)
        bl.add_widget(self.w2)
        bl.add_widget(self.w3)

        al.add_widget(bl)

        self.sm = ScreenManager()

        self.sc1 = Screen(name='firstscreen')
        self.sc1.add_widget(al)

        self.menu = AnchorLayout(anchor_y='bottom')
        self.box = BoxLayout(orientation='vertical', size_hint=[.5, .125])
        self.bottommenu = BoxLayout(orientation='horizontal')
        self.topmenu = BoxLayout(orientation='horizontal')

        self.enc = Button(text='Тарабарщина', on_press=self.entarabartion)
        self.topmenu.add_widget(self.enc)

        self.openfile = Button(text='Открыть', on_press=self.ReadFromFile)
        self.saveas = Button(text='Сохранить как', on_press=self.SaveAsFile)
        self.bottommenu.add_widget(self.openfile)
        self.bottommenu.add_widget(self.saveas)
        self.z1 = TextInput(text='Место для вашего текста...', font_size=30, multiline=False)

        self.box.add_widget(self.topmenu)
        self.box.add_widget(self.bottommenu)

        self.menu.add_widget(self.box)

        self.sc2 = Screen(name='secscreen')
        self.sc2.add_widget(self.z1)
        self.sc2.add_widget(self.menu)


        self.sm.add_widget(self.sc1)
        self.sm.add_widget(self.sc2)

        return self.sm

    def btn_press(self, instance):
        print(instance.text, self.w1.text, self.w2.text)
        print('Нажатие')
        checkme = checkSQL(self.w1.text, self.w2.text)
        try:
            if checkme[1] == self.w2.text:
                self.sm.current = 'secscreen'
        except:
            pass

    def entarabartion(self, instance):
        string = self.z1.text
        global key
        encript_string = ''
        for letter in string:
            encript_string += chr(ord(letter) ^ key)
            self.z1.text = encript_string

    def ReadFromFile(self, instance):
        from tkinter import Tk
        from tkinter import filedialog as fd

        root = Tk()
        root.withdraw()
        file_name = fd.askopenfilename()
        f = open(file_name)
        self.z1.text = f.read()
        f.close()

    def SaveAsFile(self, instance):
        from tkinter import Tk
        from tkinter import filedialog as fd

        root = Tk()
        root.withdraw()
        file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"), ("HTML files", "*.html;*.htm"), ("All files", "*.*")))
        f = open(file_name, 'w')
        f.write(self.z1.text)
        f.close()


if __name__ == "__main__":
    MyApp().run()
