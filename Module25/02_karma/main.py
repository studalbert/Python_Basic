# TODO здесь писать код
import random
class KillError(Exception):
    pass
class DrunkError(Exception):
    pass
class CarCrashError(Exception):
    pass
class GluttonyError(Exception):
    pass
class DepressionError(Exception):
    pass
class Carma:
    __CONSTANT = 500
    def get_constant(self):
        return self.__CONSTANT

    def one_day(self):
        carma = random.randint(1,7)
        if random.randint(1,10) == 1:
            err = random.choice((KillError, DrunkError, CarCrashError, GluttonyError, DepressionError))
            raise err('Карма испорчена!')
        return carma


carma = 0
with open('karma.log', 'w', encoding='utf-8') as file:
    while carma < Carma.get_constant(Carma):
        try:
            carma += Carma.one_day(Carma)
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            file.write(f'{type(exc)}, {exc}\n')
            print(type(exc))




