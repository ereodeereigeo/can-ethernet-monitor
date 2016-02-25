import glob
import sys
import os

try:
    import PySide
    comando = 'pyside-uic -o {} {}'
except ImportError:
    import PyQt4
    comando = 'pyuic4 -o {} {}'


PATH = os.path.dirname(os.path.abspath(__file__))
PATH_DESIGNER = os.path.join(PATH, 'designer')
PATH_DIALOGS = os.path.join(PATH, 'dialogs')
PATH_MAIN = os.path.join(PATH, 'mainwindow')

lista_dialogs = glob.glob(os.path.join(PATH_DESIGNER, 'dialog*'))
mainwindow = glob.glob(os.path.join(PATH_DESIGNER, 'main*'))

for dialogo in lista_dialogs:
    path_salida = os.path.join(PATH_DIALOGS, os.path.splitext(os.path.basename(dialogo))[0] + '.py')
    cmd = comando.format(path_salida, dialogo)
    print(cmd)
    os.system(cmd)


for window in mainwindow:
    path_salida = os.path.join(PATH_MAIN, os.path.splitext(os.path.basename(window))[0] + '.py')
    cmd = comando.format(path_salida, window)
    print(cmd)
    os.system(cmd)


if __name__ == '__main__':
    pass
