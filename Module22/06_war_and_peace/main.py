# TODO здесь писать код
import os
import zipfile
with zipfile.ZipFile('voina-i-mir.zip', 'r') as myzip:
    with myzip.open('voyna-i-mir.txt') as file:
        book = file.read().decode('utf-8')

myzip.close()
sym_set = set(book)
print(sym_set)
sym_set_copy = sym_set.copy()
for sym in sym_set_copy: #Оставляем только буквы в множестве
    if not sym.isalpha():
        sym_set.discard(sym)
print(sym_set)
del sym_set_copy
sym_count = 0
result_dict = dict()
for sym in sym_set: #Словарь {кол-во : символ} и считаем общее кол-во букв
    result_dict[book.count(sym)] = sym
    sym_count += book.count(sym)
result_file = open('result_file.txt', 'w', encoding='utf-8')
for quantity, sym in sorted(result_dict.items()):#Записываем результат в новый документ result_file.txt
    result_file.write(f'{sym} : {quantity}\n')

result_file.close()


