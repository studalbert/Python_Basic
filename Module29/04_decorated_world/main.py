# TODO здесь писать код
import functools
from typing import Callable, Any


def decorator_with_args_for_any_decorator(decorator:Callable) ->Callable:
    """
    Декоратор для декораторов: он должен декорировать другую функцию,
    которая должна быть декоратором, и даёт возможность
    любому декоратору принимать произвольные аргументы
     """
    @functools.wraps(decorator)
    def wrapper(*args, **kwargs) -> Callable:
        print('Переданные арги и кварги в декоратор:', args, kwargs)
        return decorator
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs)-> Callable:
    """ Декоратор, принимающий в себя произвольные аргументы """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return func(*args, **kwargs)
    return wrapper



@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)