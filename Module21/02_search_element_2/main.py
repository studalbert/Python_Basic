# TODO здесь писать код
site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def search_value(key, dct, deep = 3):
    deep -= 1
    if deep < 0:
        return None
    if isinstance(dct, dict):
        if key in dct:
            return dct[key]
    else:
        return None

    for value in dct.values():
        if search_value(key, value, deep):
            result = search_value(key, value, deep)
            return result

key = input('Введите искомый ключ: ')
deep_ask = input('Хотите ввести Хотите ввести максимальную глубину? Y/N: ')
if deep_ask.lower() == 'n':
    result = search_value(key, site)
    print(result)
else:
    deep = int(input('Введите максимальную глубину: '))
    result = search_value(key, site, deep)
    print(result)
