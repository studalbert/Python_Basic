# TODO здесь писать код
from collections import Counter
def count_unique_characters(text:str) -> int:
    sym_dict = Counter(text.lower())
    result = sum(filter(lambda x: x if x == 1 else 0, sym_dict.values()))
    return result

if __name__ == '__main__':
    # Пример использования:
    message = "Today is a beautiful day! The sun is shining and the birds are singing."

    unique_count = count_unique_characters(message)
    print("Количество уникальных символов в строке:", unique_count)
