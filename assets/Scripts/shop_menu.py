##-Импорты-##
from tkinter import *
from tkinter import messagebox
import os, sys, platform, subprocess
import db_control as dc


##-------------------------------Подключение к данным-------------------------------##

##-Подключение к БД-##
dc.conect_db('DB')

##-Переменные-##
number = 101
project_path = os.getcwd()

if platform.system() == 'Windows': divider = '\\'
elif platform.system() == 'Linux': divider = '/'


##-Подключение к JSON-##
if dc.select('INFO.nf', 'name') == False:
    if platform.system() == 'Windows': os.system('start menu.py')
    elif platform.system() == 'Linux': subprocess.call(f'{project_path}{divider}menu.py')
    sys.exit()

player_nickname = dc.select('INFO.nf', 'name')
player_skin = dc.select('INFO.nf', 'active_skin')
player_skins = dc.select('INFO.nf', 'skins')


##-Параметры окна-##
window = Tk()
window.geometry('750x341')
window.title("Магазин")


##-------------------------------Словники-------------------------------##

id_count_skin = {
    101: 0, 102: 250, 103: 500, 104: 500, 105: 990,
    201: 3901116, 202: 1500, 203: 1500, 204: 1500, 205: 1990,
    301: 0, 302: '', 303: '', 304: '', 305: ''
}

setting = {
    101: 'player_red', 102: 'player_old_red', 103: 'player_gray', 104: 'player_green',  105: 'player_rainbow', 
    201: 'player_gelic', 202: 'player_gelic_yellow', 203: 'player_gelic_gray', 204: 'player_gelic_green', 205: 'player_gelic_rainbow',
    301: 'player_tank', 302: 'empty', 303: 'empty', 304: 'empty', 305: 'empty'
}

converter = {
    101: 0, 102: 1, 103: 2, 104: 3, 105: 4,
    201: 0, 202: 1, 203: 2, 204: 3, 205: 4,
    301: 0, 302: 1, 303: 2, 304: 3, 305: 4
}


##-------------------------------Функции-------------------------------##

##-Переходники от кнопок до обработчика-##
def com1():
    btn_all(number)
def com2():
    btn_all(number+1)
def com3():
    btn_all(number+2)
def com4():
    btn_all(number+3)
def com5():
    btn_all(number+4)


##-Функция обновления картинок и кнопок-##
def update_all():
    car1.__init__()
    car2.__init__()
    car3.__init__()
    car4.__init__()
    car5.__init__()

##-Обработчик кнопок-##
def btn_all(id_skin):
    global player_skin

    ##-Проверяем наличие скина в игрока-##
    if id_skin in player_skins:

        ##-Проверка на стоящий скин-##
        if player_skin == setting[id_skin]: messagebox.showinfo("Инвентарь", 'Этот скин уже установлен')

        else:
            dc.update('INFO.nf', 'active_skin', setting[id_skin])
            dc.update(f'{player_nickname}.nf', 'skin', setting[id_skin])

            player_skin = setting[id_skin]
            

    else:
        if dc.select(f'{player_nickname}.nf', 'coin') >= id_count_skin[id_skin]:

            player_skins.append(id_skin)
            print(player_skins)
            dc.update(f'{player_nickname}.nf', 'skin', player_skins)
            dc.update('INFO.nf', 'skins', player_skins)

            messagebox.showinfo("Магазин", 'Поздравляю с покупкой')

        else: messagebox.showinfo("Баланс", 'У тебя не хватает монеток')
        

    update_all()

##-------------------------------Классы-------------------------------##

class Car1():

    def __init__(self):
        self.update()

        car = Label(image = self.skin_photo, bg = '#00316a')
        car.place(x = 74, y = 144, width = 94, height = 126)

        car_btn = Button(text = f'{self.text_btn}', bg = f'#{self.btn_color}', command = com1)
        car_btn.place(x = 72, y = 270, width = 100, height = 39)

    def update(self):
        self.skin_photo = PhotoImage(file = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}img{divider}player{divider}{setting[number]}.png")
        
        if number in player_skins:
            if player_skin == setting[number]:
                self.text_btn = 'Используеться'
                self.btn_color = '00c46c'

            else:
                self.text_btn = 'Использовать'
                self.btn_color = '009ac4'

        else:
            self.text_btn = id_count_skin[number]
            self.btn_color = 'c400b0'

class Car2():

    def __init__(self):
        self.update()

        car = Label(image = self.skin_photo, bg = '#00316a')
        car.place(x = 197, y = 144, width = 94, height = 126)

        car_btn = Button(text = f'{self.text_btn}', bg = f'#{self.btn_color}', command = com2)
        car_btn.place(x = 195, y = 270, width = 100, height = 39)

    def update(self):
        self.skin_photo = PhotoImage(file = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}img{divider}player{divider}{setting[number+1]}.png")
        
        if number+1 in player_skins:
            if player_skin == setting[number+1]:
                self.text_btn = 'Используеться'
                self.btn_color = '00c46c'

            else:
                self.text_btn = 'Использовать'
                self.btn_color = '009ac4'

        else:
            self.text_btn = id_count_skin[number+1]
            self.btn_color = 'c400b0'

class Car3():

    def __init__(self):
        self.update()

        car = Label(image = self.skin_photo, bg = '#00316a')
        car.place(x = 324, y = 144, width = 94, height = 126)

        car_btn = Button(text = f'{self.text_btn}', bg = f'#{self.btn_color}', command = com3)
        car_btn.place(x = 322, y = 270, width = 100, height = 39)

    def update(self):
        self.skin_photo = PhotoImage(file = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}img{divider}player{divider}{setting[number+2]}.png")
        
        if number+2 in player_skins:
            if player_skin == setting[number+2]:
                self.text_btn = 'Используеться'
                self.btn_color = '00c46c'

            else:
                self.text_btn = 'Использовать'
                self.btn_color = '009ac4'

        else:
            self.text_btn = id_count_skin[number+2]
            self.btn_color = 'c400b0'

class Car4():

    def __init__(self):
        self.update()

        car = Label(image = self.skin_photo, bg = '#00316a')
        car.place(x = 452, y = 144, width = 94, height = 126)

        car_btn = Button(text = f'{self.text_btn}', bg = f'#{self.btn_color}', command = com4)
        car_btn.place(x = 450, y = 270, width = 100, height = 39)

    def update(self):
        self.skin_photo = PhotoImage(file = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}img{divider}player{divider}{setting[number+3]}.png")
        
        if number+3 in player_skins:
            if player_skin == setting[number+3]:
                self.text_btn = 'Используеться'
                self.btn_color = '00c46c'

            else:
                self.text_btn = 'Использовать'
                self.btn_color = '009ac4'

        else:
            self.text_btn = id_count_skin[number+3]
            self.btn_color = 'c400b0'


class Car5():

    def __init__(self):
        self.update()

        car = Label(image = self.skin_photo, bg = '#00316a')
        car.place(x = 567, y = 144, width = 94, height = 126)

        car_btn = Button(text = f'{self.text_btn}', bg = f'#{self.btn_color}', command = com5)
        car_btn.place(x = 565, y = 270, width = 100, height = 39)

    def update(self):
        self.skin_photo = PhotoImage(file = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}img{divider}player{divider}{setting[number+4]}.png")
        
        if number+4 in player_skins:
            if player_skin == setting[number+4]:
                self.text_btn = 'Используеться'
                self.btn_color = '00c46c'

            else:
                self.text_btn = 'Использовать'
                self.btn_color = '009ac4'

        else:
            self.text_btn = id_count_skin[number+4]
            self.btn_color = 'c400b0'


##Вызов классов##
car1 = Car1()
car2 = Car2()
car3 = Car3()
car4 = Car4()
car5 = Car5()


##-------------------------------Кнопки и обработчики к ним-------------------------------##

##Кнопка ">" и её обработчик##
def next_c():
    global number

    if number < 301: number += 100
    update_all()

next_btn = Button(text = '>', command = next_c, font = 'Times 30', bg = '#00316a')
next_btn.place(x = 680, y = 166)


##Кнопка "<" и её обработчик##
def back():
    global number

    if number >= 301 or number >= 201: number -= 100
    update_all()

back_btn = Button(text = '<', command = back, font = 'Times 30', bg = '#00316a')
back_btn.place(x = 10, y = 166)


##Кнопка "<(exit)" и её обработчик##
def ex():
    os.remove(f"{project_path}{divider}DB{divider}INFO.nf")
    window.destroy()
    if platform.system() == 'Windows': os.system('start menu.py')
    elif platform.system() == 'Linux': subprocess.call(f'{project_path}{divider}menu.py')

ex_btn = Button(text = '<', bg = '#00316a', command = ex, font = 'Times 30')
ex_btn.place(x = 12, y = 11, width = 64, height = 64)


##Отображение монеток##
money = dc.select(f'{player_nickname}.nf', 'coin')

player_money = Label(text = money, bg = '#00316a', font = 'Times 25')
player_money.place(x = 560, y = 32, width = 159, height = 56)

img_pouch = PhotoImage(file = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}img{divider}items{divider}money_pouch.png")
player_money_pouch = Label(bg = '#00316a', image = img_pouch)
player_money_pouch.place(x = 560, y = 39, width = 36, height = 41)


window.config(background = '#004ca3')
window.mainloop()
