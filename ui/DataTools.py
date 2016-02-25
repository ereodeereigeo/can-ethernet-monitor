import os
BASEPATH = os.path.dirname(os.path.abspath(__file__))

PATH_DATOS = os.path.join(BASEPATH, 'data')

if not os.path.exists(PATH_DATOS):
    os.mkdir(PATH_DATOS)

class DataBase(object):
    pass