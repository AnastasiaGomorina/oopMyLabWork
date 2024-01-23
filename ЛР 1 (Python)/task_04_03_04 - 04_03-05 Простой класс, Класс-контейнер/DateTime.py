# Программирование на языке высокого уровня (Python).
# Задание №4.3.4. - 4.3.5 Вариант 5
#
# Выполнила: Гоморина А.В.
# Группа: ПИН-б-о-21-1
# E-mail: nastyagomorinalove@gmail.com


import json
from datetime import datetime, timedelta


class DateTime:
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        min_date = datetime.min
        self._datetime = min_date.replace(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

    def __str__(self):
        return self._datetime.strftime("%Y-%m-%d %H:%M:%S")

    def __add__(self, other):
        if isinstance(other, DateTime):
            result = self._datetime + timedelta()
            return DateTime(result.year, result.month, result.day, result.hour, result.minute, result.second)
        raise TypeError("Unsupported operand type for +: 'DateTime' and {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, DateTime):
            result = self._datetime - timedelta()
            return DateTime(result.year, result.month, result.day, result.hour, result.minute, result.second)
        raise TypeError("Unsupported operand type for -: 'DateTime' and {}".format(type(other)))

    @classmethod
    def from_string(cls, str_value):
        dt = datetime.strptime(str_value, "%Y-%m-%d %H:%M:%S")
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self._datetime.strftime("%Y-%m-%d %H:%M:%S"), file)

    def load(self, filename):
        with open(filename, 'r') as file:
            str_value = json.load(file)
            dt = datetime.strptime(str_value, "%Y-%m-%d %H:%M:%S")
            self._datetime = dt

    @property
    def year(self):
        return self._datetime.year

    @property
    def month(self):
        return self._datetime.month

    @property
    def day(self):
        return self._datetime.day

