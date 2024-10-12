# TODO здесь писать код
class MyMath:
    """ Класс-аналог модуля math """

    @classmethod
    def circle_len(cls, radius: int|float) -> float:
        """" вычисление длины окружности """
        len = 2 * 3.14 * radius
        return round(len, 2)

    @classmethod
    def circle_sq(cls, radius: int|float)-> float:
        """ вычисление площади окружности """
        sq = 3.14 * radius**2
        return round(sq, 2)

    @classmethod
    def volume_cube(cls, side: int|float)-> float:
        """ вычисление объёма куба """
        volume = side ** 3
        return volume

    @classmethod
    def area_sphere(cls, radius: int|float)-> float:
        """ вычисление площади поверхности сферы. """
        area = 4 * 3.14 * radius**2
        return round(area, 2)

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)





