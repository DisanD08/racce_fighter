##Импорты##
import platform, os, subprocess, json


##Проверка ОС##
if platform.system() == 'Windows': divider = '\\'
elif platform.system() == 'Linux': divider = '/'


##Переменные##
path = os.getcwd()#     <- Путь к основй папке(на данный момент онa рабочая)


if not os.path.exists(f'{path}{divider}assets{divider}Scripts{divider}DB{divider}PH.nf'):
    f = open(f'{path}{divider}assets{divider}Scripts{divider}DB{divider}PH.nf', 'a')
    data_json = {
        "path": f'{path}'
    }
    data_dumps = json.dumps(data_json, sort_keys=True, indent=4, ensure_ascii=False)
    f.write(data_dumps)
    f.close()


if platform.system() == 'Windows': os.system(f'start {path}{divider}assets{divider}Scripts{divider}menu.py')
elif platform.system() == 'Linux': subprocess.call(f'{path}{divider}assets{divider}Scripts{divider}menu.py')
