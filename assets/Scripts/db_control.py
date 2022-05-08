##-Импорты-##
import os, platform, json

##-Узнаем нужные полосы юзера-##
if platform.system() == 'Windows': divider = '\\'
elif platform.system() == 'Linux': divider = '/'

##-Переменные-##
project_path = os.getcwd()


#-------------------------------Работа из БД-------------------------------#

##-Подключение в БД-##
def conect_db(name):
    global db_path
    db_path = f'{project_path}{divider}{name}'

##-Создание БД-##
def creat_db(name):

    if not os.path.isdir(name):
        name = str(name)
        os.mkdir(name)

        return True

    else: return False

##-Удаление БД-##
def remove_db(name):

    try:
        os.rmdir(f'{project_path}{divider}{name}')

        return True

    except Exception as ex:
        print('-'*80)
        print(f'Ошибка удаления базы данных {name}\nОшибка:\n{ex}')
        print('-'*80)

        return False


#-------------------------------Работа из таблицами-------------------------------#

##-Читаем файл-##
def read(name):
    try:
        file = open(f'{db_path}{divider}{name}')
        data = file.read()
        data_json = json.loads(data)
        file.close()

        return data_json

    except Exception as ex:
        print('-'*80)
        print(f'Ошибка читаемости файла\nОшибка:\n{ex}')
        print('-'*80)

        return False

##-Запись в файл-##
def write(name, data_json):

    try:
        data_dumps = json.dumps(data_json, sort_keys=True, indent=4, ensure_ascii=False)
        file = open(f'{db_path}{divider}{name}', "w")
        file.write(data_dumps)
        file.close()

        return True

    except Exception as ex:
        print('-'*80)
        print('Ошибка записи данных:  ', ex)
        print('-'*80)

        return False

##-Создание и удаление таблицы-##
def creat_table(name):

    if not os.path.exists(f'{db_path}{divider}{name}'):
        file = open(f'{db_path}{divider}{name}', 'w')
        file.write('{}')
        file.close()

        return True

    return False

def remove_table(name):

    try:
        os.remove(f'{db_path}{divider}{name}')

        return True

    except Exception as ex:
        print('Ошибка удаления таблицы', name)

        return False


##-Обновление данных-##
def update(name, key, new_value):
    data_json = read(name)

    data_json[key] = new_value

    write(name, data_json)

##-Поис данных-##
def select(name, key):
    data_json = read(name)

    try:
        if key == '*':
            result = data_json
        else:
            result = data_json.get(key, False)#f'Отсутсувет столбик {key}')

        return result

    except Exception as ex:
        print('-'*80)
        print('Произошла неизвестная ошибка:  ', ex)
        print('-'*80)

        return False
    
    return {}


##-Ввод данных-##
def insert(name, kwargs):
    data_json = read(name)

    if type(kwargs) == dict:
        data_json.update(kwargs)
        write(name, data_json)

##-Удаленние данных-##
def delete(name, key):
    data_json = read(name)

    try:
        data_json.pop(key)
        write(name, data_json)

        return True

    except Exception as ex:
        print('-'*80)
        print('Ошибка удаления данных\nОшибка:  ', ex)
        print('-'*80)
         
        return False
