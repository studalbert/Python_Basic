# TODO здесь писать код
file = open('text.txt', 'r')
file_str = file.read().rstrip('.')
file.close
file_lst = file_str.split()
file_str = ''.join(file_lst).lower()
file_set = set(file_str)
result = dict()
for sym in file_set:
    procent = round((file_str.count(sym) / len(file_str)), 3)
    result[sym] = procent

analysis = open('analysis.txt', 'w')
values_dct_sort = sorted(result.values(), reverse=True)
print(values_dct_sort)

for value in values_dct_sort:
    for key in sorted(result.keys()):
        if result[key] == value:
            analysis.write(f'{key} : {value}\n')
            result.pop(key)
            break

analysis.close()