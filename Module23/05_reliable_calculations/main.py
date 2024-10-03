# TODO здесь писать код

# Здесь создайте функцию get_sage_sqrt
def get_sage_sqrt(num):
    try:
        if not isinstance(num, (int, float)):
            raise TypeError('Число не может состоять из букв')
        if num < 0:
            raise ValueError('Число не может быть меньше нуля')
        return num ** (1/2)
    except ValueError as exc:
        return f'{type(exc)}, {exc}'

    except TypeError as exc:
        return f'{type(exc)}, {exc}'

# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")