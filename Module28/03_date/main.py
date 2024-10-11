# TODO здесь писать код
from datetime import datetime
class Date:
    _date = None

    def __str__(self) -> str:
        date_lst = self._date.split('-')
        return f'День: {date_lst[0]}\tМесяц: {date_lst[1]}\tГод: {date_lst[2]}'


    @property
    def date(self)-> str:
        return self._date

    @date.setter
    def date(self, date) -> None:
        self._date = date

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        date_format = '%d-%m-%Y'
        try:
            if datetime.strptime(date_str, date_format):
                return True
        except Exception:
            return False

    @classmethod
    def from_string(cls, date_str:str) -> 'Date':
        if not cls.is_date_valid(date_str):
            raise ValueError('Некорректная дата')
        cls._date = date_str
        return Date()

date = Date.from_string('12-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

