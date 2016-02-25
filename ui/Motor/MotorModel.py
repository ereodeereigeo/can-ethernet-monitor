
class MotorModel(object):

    def __init__(self):
        super(MotorModel, self).__init__()
        self.__dict_status = dict()

    def __getattr__(self, attr):
        return attr

    def __setitem__(self, key, value):
        pass