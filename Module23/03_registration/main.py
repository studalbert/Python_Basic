# TODO здесь писать код
line_count = 0
with open('registrations.txt', 'r', encoding='utf-8') as registrations:
    for line in registrations:
        line_count += 1
        registrations_lst = line.rstrip().split()
        try:
            if len(registrations_lst) != 3:
                raise IndexError
            if not registrations_lst[0].isalpha():
                raise NameError
            if '@' not in registrations_lst[1] or '.' not in registrations_lst[1]:
                raise SyntaxError
            if int(registrations_lst[2]) < 10 or int(registrations_lst[2]) > 99:
                raise ValueError
            with open('registrations_good.log', 'a', encoding='utf-8') as registrations_good:
                registrations_good.write(f"{' '.join(registrations_lst)}\n")
        except IndexError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as registrations_bad:
                registrations_bad.write(f'в строке {line_count} НЕ присутствуют все три поля\n')
        except  NameError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as registrations_bad:
                registrations_bad.write(f'в строке {line_count} Поле «Имя» содержит НЕ только буквы\n')
        except  SyntaxError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as registrations_bad:
                registrations_bad.write(f'в строке {line_count} Поле «Имейл» НЕ содержит @ и . (точку)\n')
        except  ValueError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as registrations_bad:
                registrations_bad.write(f'в строке {line_count} Поле «Возраст» НЕ является числом от 10 до 99\n')