# TODO здесь писать код

result_summ = 0
with open('people.txt', 'r', encoding='utf-8') as people:
    line_count = 0
    for line in people:
        line_count += 1
        try:
            if len(line[:-1]) < 3:
                raise BaseException(f'В {line_count} строке ошибка: менее трех символов.')
            result_summ += len(line[:-1])
        except BaseException as exc:
            print(f'В {line_count} строке ошибка: менее трех символов.')
            with open('errors.log', 'a', encoding='utf-8') as error:

                error.write(f'В {line_count} строке ошибка:{type(exc)} менее трех символов.\n')

print('Общее количество символов:', result_summ)