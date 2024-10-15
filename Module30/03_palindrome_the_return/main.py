# TODO здесь писать код
from collections import Counter
def can_be_poly(text:str) -> bool:
    result = list(filter(lambda x: None if x % 2 == 0 else True, Counter(text).values()))
    if len(result) <= 1:
        return True
    else:
        return False

if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
