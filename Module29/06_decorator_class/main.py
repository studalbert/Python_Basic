# TODO здесь писать код
import functools
import time
from collections.abc import Callable


class LoggerDecorator:
    """ Класс-декоратор, который логирует аргументы, результаты и время выполнения декорируемой функции """
    def __init__(self, func:Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> Callable:
        print(f'Вызов функции {self.func.__name__}')
        print(f'Аргументы:', args, kwargs)
        start = time.time()
        result = self.func(*args, **kwargs)
        run_time = time.time() - start
        print('Результат:', result)
        print('Время выполнения:', run_time)


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)

