# TODO здесь писать код

class LRUCache:
    """
    класс LRU Cache,
    который хранит ограниченное количество объектов и,
    при превышении лимита,
    удаляет самые давние (самые старые) использованные элементы.
    Args and attrs:
        capacity (int): вместимость списка _cache
        _cache_counter (dict): словарь, ключи которого элементы из списка _cache, а значения - количество запросов к этим элементам
        _cache (list): список элементов
     """
    def __init__(self,capacity:int) -> None:
        self.capacity = capacity
        self._cache_counter = dict()
        self._cache = [None] * self.capacity

    @property
    def cache(self) -> tuple:
        """ Геттер. возвращает самый старый элемент """
        min_count = min(self._cache_counter.values())
        for key in self._cache_counter:
            if self._cache_counter[key] == min_count:
                return key


    @cache.setter
    def cache(self, elem:tuple) -> None:
        """ Сеттер. метод должен добавлять новый элемент в список  """
        if None not in self._cache:
            self.del_elem()
        for i in range(len(self._cache)):
            if not self._cache[i]:
                self._cache[i] = elem
                if elem not in self._cache_counter:
                    self._cache_counter[elem] = 1
                else:
                    self._cache_counter[elem] += 1
                break

    def del_elem(self) -> None:
        """ Метод удалает давно использованный элемент из списка  """
        min_count = min(self._cache_counter.values())
        for key in self._cache_counter:
            if self._cache_counter[key] == min_count:
                self._cache.remove(key)
                self._cache_counter.pop(key)
                break
        self._cache.append(None)

    def print_cache(self) -> None:
        """" Печатает на экран элементы списка """
        print('LRU Cache')
        for key, value in self._cache:
            print(f'{key} : {value}')
        print()

    def get(self, user_key:str) -> str:
        """" Метод возвращает значение по ключу """
        for key, value in self._cache:
            if key == user_key:
                self._cache_counter[(key, value)] += 1
                return value
        else:
            return f'Такого ключа нет'



# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4

cache.cache = ("key5", "value5")
cache.print_cache()