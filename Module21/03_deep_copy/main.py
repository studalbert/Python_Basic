# TODO здесь писать код
def result_site(product):
    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам телефон недорого'
            },
            'body': {
                'h2': f'У нас самая низкая цена на {product}',
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }
    return site
sites_count = int(input('Сколько будет сайтов? '))
result = []
for i in range(sites_count):
    product = input('Введите название продукта для нового сайта: ')
    result.append(result_site(product))
    print(result)


#Или:

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2':  'У нас самая низкая цена на Iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
def deep_copy(obj, product):
    if obj == 'У нас самая низкая цена на Iphone':
        obj = f'У нас самая низкая цена на {product}'
        return obj
    if isinstance(obj, (str, int, float, bool)):
        return obj

    elif isinstance(obj, dict):
        result = {key:deep_copy(value, product) for key, value in obj.items()}
        return result


sites_count = int(input('Сколько будет сайтов? '))
result = []
for i in range(sites_count):
    product = input('Введите название продукта для нового сайта: ')
    result.append(deep_copy(site, product = product))
    print(result)

