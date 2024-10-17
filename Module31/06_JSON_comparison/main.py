# TODO здесь писать код
import json

diff_list = ["services", "staff", "datetime"]

print('Данные, загруженные из json_old.json:')
with open('json_new.json', 'r', encoding='utf-8') as file:
    data_new = json.load(file)
print(data_new)

print('Данные, загруженные из json_new.json:')
with open('json_old.json', 'r', encoding='utf-8') as file:
    data_old = json.load(file)
print(data_old)

print('Вывод результата:')
result = {elem : data_new['data'][elem] for elem in diff_list if data_old['data'][elem] != data_new['data'][elem]}
print(result)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4)