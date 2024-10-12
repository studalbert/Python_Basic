# TODO здесь писать код
import os
class File:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        if os.path.exists(self.file_name):
            self.file = open(self.file_name, self.mode, encoding='utf-8')
            return self.file
        else:
            self.mode = 'w'
            self.file = open(self.file_name, self.mode, encoding='utf-8')
            return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('example.txt', 'r') as file:
    print(file.read())