# TODO здесь писать код
import functools
import time
from collections.abc import Callable
from datetime import datetime
# def logging(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'Запускается {func.__name__}. Дата и время запуска: {date}')
#         start = time.time()
#         result = func(*args, **kwargs)
#         run_time = time.time() - start
#         print(f'Завершение {func.__name__}. время работы = {round(run_time, 3)}')
#     return wrapper


def log_methods(date:str) -> Callable:
    """
    Декоратор, который будет логировать все методы декорируемого класса (кроме магических методов)
    и в который можно передавать формат вывода даты и времени логирования.
    """
    def logging(func:Callable):
        """ Декоратор, который будет применяться к каждому методу классов """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            date_format = ''
            for sym in date:
                if sym in alphabet:
                    date_format += f'%{sym}'
                else:
                    date_format += sym
            print(f'Запускается {func.__qualname__}. Дата и время запуска: {datetime.strftime(datetime.now(), format = date_format)}')
            start = time.time()
            result = func(*args, **kwargs)
            run_time = time.time() - start
            print(f'Завершение {func.__qualname__}. время работы = {round(run_time, 3)}s')
        return wrapper

    def decorator(cls):
        """ Функция, благодаря который мы будем проходить по кажому методу класса и декорировать их """
        for method in dir(cls):
            if method.startswith('__') is False:
                cur_method = getattr(cls, method)
                new_method = logging(cur_method)
                setattr(cls, method, new_method)
        return cls
    return decorator



@log_methods(date="b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods(date="b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()