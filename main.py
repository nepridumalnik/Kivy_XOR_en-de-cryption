import sqlite3

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView


class MenuScreen(Screen):
    pass


class Next(Screen):
    pass

class AdPan(Screen):
    pass

class Row():
    pass

def entarabartion(string):
    tarabara = """ 1234567890-=!@#$%^&*()_+!"№;%:?*(),./\|QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>[];'qwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэжячсмитьбю."""
    ntext = ''
    for letter in string:
        ntext += tarabara[tarabara.find(letter) * (-1)]
    return ntext

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
        print(checkme[2])
        try:
            if checkme[0] == self.w1.text and checkme[1] == self.w2.text:
                self.sm.current = 'secscreen'
                if checkme[2] == 'admin':
                    self.adminpanel = Button(text='Админская панель', on_press=self.Admpan)
                    self.bottommenu.add_widget(self.adminpanel)
                    self.sc3 = Screen(name='adminpanel')
                    self.sm.add_widget(self.sc3)
                    print('Adminpanel suc created')

        except:
            pass

    def Admpan(self, instance):
        print('Admin table')
        self.sm.current = 'adminpanel'
        self.data = self.ASQL()
        print(self.data)
        self.userlist = AnchorLayout(anchor_y='top')
        self.col = BoxLayout(orientation='vertical', size_hint=(1, .2))

        for user in self.data:
            self.row = BoxLayout(orientation='horizontal')
            for u in user:
                self.row.add_widget(Button(text=u))
            self.col.add_widget(self.row)

        self.userlist.add_widget(self.col)

        self.botto = AnchorLayout(anchor_y='bottom')
        self.bom = BoxLayout(size_hint=(.4, .15))
        self.botto.add_widget(self.bom)
        self.side = BoxLayout(size_hint=(.1, 1))

        self.backonsec = Button(text='Назад', on_press=self.backonsecscr)
        self.side.add_widget(self.backonsec)
        self.horiz = BoxLayout(orientation='horizontal')

        self.scroll = ScrollView()
        self.scroll.add_widget(self.userlist)

        self.horiz.add_widget(self.side)
        self.horiz.add_widget(self.scroll)

        self.sc3.add_widget(self.horiz)

    def backonsecscr(self, instance):
        self.sm.current = 'secscreen'

    def ASQL(self):
        try:
            connect = sqlite3.connect("mydatabase.db")
        except:
            pass
        cursor = connect.cursor()

        text = "SELECT * FROM table1"

        cursor.execute(text)
        results = cursor.fetchall()

        users = []

        for result in results:
            if result not in users:
                users.append(result)

        connect.commit()
        connect.close()

        return users

    def entarabartion(self, instance):
        string = self.z1.text
        tarabara = """ 1234567890-=!@#$%^&*()_+!"№;%:?*(),./\|QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>[];'qwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэжячсмитьбю."""
        ntext = ''
        for letter in string:
            ntext += tarabara[tarabara.find(letter) * (-1)]
            self.z1.text = ntext

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
