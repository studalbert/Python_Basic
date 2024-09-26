# TODO здесь писать код
def prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            return True


def crypto(your_object):
    return [value for index, value in enumerate(your_object) if prime(index)]

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))