# TODO здесь писать код
class MyDict(dict):
    def __init__(self, dict):
        self.__dict__ = dict

    def get(self, key):
        if self.__dict__.get(key) == None:
            return 0
        else:
            return self.__dict__.get(key)


my_dict = MyDict({'a': 1234, 'b': 214, 'c': 1455})
print(my_dict.get('b'))
print(my_dict.get('f'))