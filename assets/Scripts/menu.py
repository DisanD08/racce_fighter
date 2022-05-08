##-Импорты-##
from tkinter import *
from tkinter import messagebox
import sys, os, json, platform, subprocess
import db_control as dc

##-Переменные-##
project_path = os.getcwd()

##-Узнаем ОС юзера-##
if platform.system() == 'Windows': divider = '\\'
elif platform.system() == 'Linux': divider = '/'

##-Параметры окна-##
window = Tk()
window.geometry('366x528')
window.title('Меню')

##Подключение к базе данных##
dc.conect_db('DB')


#-------------------------------Обработчики-------------------------------#


def start_game():
    name = ent.get()

    if name == 'DisanD_0': messagebox.showinfo("FUCK YOU", "Вы не создатель!")

    elif name== '': messagebox.showinfo("ERROR", "Поле не может быть пустым!")

    else:
        if dc.select(f'{name}.nf', 'name') == False: print('ERROR 404')
        else:

            user = {"name": name, "active_skin": dc.select(f'{name}.nf', 'skin')}

            dc.creat_table('INFO.nf')
            dc.insert('INFO.nf', user)

            if platform.system() == 'Windows': os.system(f'start {project_path}{divider}racce.py')
            elif platform.system() == 'Linux': subprocess.call(f'{project_path}{divider}racce.py')
            window.destroy()

def shop_command():
    name = ent.get()

    if name == 'DisanD_0': messagebox.showinfo("FUCK YOU", "Вы не создатель!")

    elif name== '': messagebox.showinfo("ERROR", "Поле не может быть пустым!")

    else:
        if dc.select(f'{name}.nf', 'name') == False: print('ERROR 404')
        else:

            user = {"name": name, "skins": dc.select(f'{name}.nf', 'skins'), "active_skin": dc.select(f'{name}.nf', 'skin')}

            dc.creat_table('INFO.nf')
            dc.insert('INFO.nf', user)

            if platform.system() == 'Windows': os.system(f'start {project_path}{divider}shop_menu.py')
            elif platform.system() == 'Linux': subprocess.call(f'{project_path}{divider}shop_menu.py')
            window.destroy()

##Обработчик кнопки "Об игре"##
def info_for_game(): messagebox.showinfo("Об игре", 'Игру создали: DisanD_08(еблан редкостный), ko6pa и самый главный про нашей группы hearty\n\nКартинки рисовали: DisanD_08 и ko6pa\n\nНасчет игры, я вам соболезную что вам пришлось играть в эту говно-игру, могу вам только пожелать удачи, и еще хочу сказать что игра в разработке, мб где-то оствалю и ссылку на канал, хотя вы наверно из него игру и взяли, так-что смысла нет')

##Обработчик кнопки "Донат"##
def donat_def(): messagebox.showinfo("DONATE", 'Ты реально хочешь задонатить в эту говно игру?\nЯ почтен, только знать бы еще как это сделать')

##Обработчик кнопки "Выход"##
def exit_in_game(): window.destroy()


#-------------------------------Kнопки-------------------------------#

##Кнопка "Играть"##
game_btn = Button(text = 'Играть', bg='DarkGoldenrod1', command = start_game, cursor = 'diamond_cross')
game_btn.place(x = 104, y = 278, width =  150, height = 50)

##Кнопка "Магазин"##
shop_btn = Button(text = 'Магазин', bg='DarkGoldenrod1', command = shop_command)
shop_btn.place(x = 18, y = 336, width = 150, height = 50)

##Пустаня кнопка, нужная только для дизайна##
empty_heug_btn = Button(bg='DarkGoldenrod1')
empty_heug_btn.place(x = 187, y = 336, width = 150, height = 50)

##Кнопка "Об игре"##
info_game_btn = Button(text = 'Об игре', bg='DarkGoldenrod1', command = info_for_game)
info_game_btn.place(x = 18, y = 410, width = 150, height = 50)

##Кнопка "Донат"##
donat_btn = Button(text = 'Донат', bg='DarkGoldenrod1', command = donat_def)
donat_btn.place(x = 187, y = 410, width = 150, height = 50)

##Кнопка "Выход"##
exit_btn = Button(text = 'Выход', bg='DarkGoldenrod1', command = exit_in_game, cursor = 'X_cursor')
exit_btn.place(x = 104, y = 468, width = 150, height = 50)


#-------------------------------Отрисовка данных об игроке-------------------------------#

##Отрисовка полей для данных##
lbox_name = Listbox(bg='RoyalBlue2')
lbox_name.place(x = 13, y = 116, width = 114, height = 150)

lbox_score = Listbox(bg='RoyalBlue2')
lbox_score.place(x = 128, y = 116, width = 104, height = 150)

lbox_coin = Listbox(bg='RoyalBlue2')
lbox_coin.place(x = 233, y = 116, width = 91, height = 150)

##Подписи для полей##
info1 = Label(text = f'Имя:', bg='chartreuse4')
info1.place(x = 13, y = 76, width = 115, height = 30)

info2 = Label(text = f'Счёт:', bg='chartreuse4')
info2.place(x = 128, y = 76, width = 104, height = 30)

info3 = Label(text = f'Монетки:', bg='chartreuse4')
info3.place(x = 232, y = 76, width = 91, height = 30)


##Функция заполнения полей данными##


##Надпись "Имя" возле ввода##
name_label = Label(text = f'Имя:', bg='tomato')
name_label.place(x = 21, y = 16, width = 100, height = 30)

##Показатель версии игры и всех файлов директории##
vv = Label(text = '0.1.4', bg='green3')
vv.place(x = 329, y = 510)

##Поле для ввода##
ent = Entry(justify = "center", font = "14", bg='orange red', fg = 'blue')
ent.place(x = 137, y = 14, width = 215, height = 35)


window.configure(background='green3')
window.mainloop()
