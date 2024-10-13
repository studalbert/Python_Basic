# TODO здесь писать код
import functools
from typing import Callable, Any

app = {}
def callback(event:str) -> Callable:
    def decorator(func:Callable) -> Callable:
        app[event] = func
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            return func(*args, **kwargs)
        return wrapped
    return decorator

@callback(event = '//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')