from pathlib import Path
from os import listdir
from importlib import import_module

path_parent = Path('./app/routers')

for module in listdir(path_parent):
    if 'router' in module:
        # print(module[:-3])
        import_module(f'app.routers.{module[:-3]}')