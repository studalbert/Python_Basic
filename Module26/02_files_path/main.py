# TODO здесь писать код
import os.path
from collections.abc import Iterator

path = os.path.abspath(os.path.join('..', '02_files_path'))

def gen_files_path(path: str) -> Iterator[str]:
    for root, dirs, files in os.walk(os.path.abspath(os.path.join('..', '..', '..', 'Python_Basic'))):
        # print(f'Каталог: {root}')
        # print(f'Подкаталоги: {dirs}')
        # print(f'Файлы: {files}')
        # print('==================================================================')
        if root == path:
            for file in files:
                yield file
# gen_files_path(path)
for file in gen_files_path(path):
    print(file)
