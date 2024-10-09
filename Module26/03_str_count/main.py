# TODO здесь писать код
import os
from collections.abc import Iterator
# file_path = os.path.abspath(os.path.join('..', '..', '..', 'pythonProject8', 'lesson 13.5.py'))
def gen_files_path() -> Iterator[tuple[str, int]]:
    for root, dirs, files in os.walk(os.path.abspath(os.path.join('..', '..', '..', 'pythonProject8'))):
        for file in files:
            if file.endswith('.py'):
                # if os.path.join(root, file) == file_path:
                file_line_count = 0
                with open(os.path.join(root, file), 'r', encoding='utf-8') as i_file:
                    for line in i_file:
                        if len(line.rstrip()) > 0 and not line.startswith('#'):
                            file_line_count += 1
                yield os.path.join(root, file), file_line_count


for file_path, line_count in gen_files_path():
    print(f'Файл: {file_path}\t Количество строк: {line_count}')
