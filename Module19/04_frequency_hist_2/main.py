# TODO здесь писать код
def  new_hist(hist):
    invert_hist = dict()
    for value in hist.values():
        invert_hist[value] = [key for key in hist.keys() if hist[key] == value]
    return invert_hist
text = input('Введите текст: ')
hist = dict()
for sym in text:
    if sym in hist:
        hist[sym] += 1
    else:
        hist[sym] = 1
print('Оригинальный словарь частот:')
for k in sorted(hist.keys()):
    print(f'{k}:{hist[k]}' )

print('Инвертированный словарь частот:')
for key in new_hist(hist):
    print(f'{key} : {new_hist(hist)[key]}')