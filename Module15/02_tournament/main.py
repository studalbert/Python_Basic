# TODO здесь писать код
names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
result = []
for i in range(len(names)):
    if i % 2 == 0:
        result.append(names[i])
print(f'Первый день: {result}')