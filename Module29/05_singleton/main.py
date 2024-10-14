# TODO здесь писать код
import functools


def singleton(cls):
    """
    Декоратор, который превращает класс
    в одноэлементный.
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if wrapper.instance:
            return wrapper.instance
        instance = cls(*args, **kwargs)
        wrapper.instance = instance
        return instance
    wrapper.instance = None
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)