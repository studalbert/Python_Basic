# TODO здесь писать код
import functools
from typing import Callable, Any, Optional

user_permissions = ['admin']

def check_permission(_func:Optional[Callable] = None, *, permission:str) -> Callable:
    """
     Декоратор с аргументом permission, который проверяет, есть ли у пользователя доступ к вызываемой функции,
     и если нет, то выдаёт исключение PermissionError
    """
    def decorator(func:Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            if permission == user_permissions[0]:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')

        return wrapped
    if _func is None:
        return decorator
    return decorator(_func)



@check_permission(permission='admin')
def delete_site():
    print('Удаляем сайт')

@check_permission(permission='user_1')
def add_comment():
    print('Добавляем комментарий')

try:
    delete_site()
    add_comment()
except PermissionError as exc:
    print(type(exc), exc)