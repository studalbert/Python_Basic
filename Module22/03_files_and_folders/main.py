# TODO здесь писать код
import os
path = os.path.abspath(os.path.join('..','..','Module14'))
size_dir = [0]
count_dir = [0]
count_file = [0]
def result(path):
    for i_elem in os.listdir(path):
        new_path = os.path.join(path, i_elem)
        if os.path.isdir(new_path):
            count_dir[0] += 1
            result(new_path)
        elif os.path.isfile(new_path):
            count_file[0] += 1
            size_dir[0] += os.path.getsize(new_path)
result(path)
print(path)
print('Размер каталога (в Кб):', round((size_dir[0]/1024), 2))
print('Количество файлов:', count_file[0])
print('Количество подкаталогов:', count_dir[0])