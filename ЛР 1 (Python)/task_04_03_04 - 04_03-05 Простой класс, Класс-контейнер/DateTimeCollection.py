# Программирование на языке высокого уровня (Python).
# Задание №4.3.4. - 4.3.5 Вариант 5
#
# Выполнила: Гоморина А.В.
# Группа: ПИН-б-о-21-1
# E-mail: nastyagomorinalove@gmail.com


import json
from DateTime import DateTime


class DateTimeCollection:
    def __init__(self):
        self._data = []

    def __str__(self):
        return ', '.join(str(item) for item in self._data)

    def __getitem__(self, index):
        return self._data[index]

    def add(self, value):
        if isinstance(value, DateTime):
            self._data.append(value)
        else:
            raise TypeError("Only DateTime objects can be added to the collection")

    def remove(self, index):
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Index out of range")

    def save(self, filename):
        data_to_save = [str(item) for item in self._data]
        with open(filename, 'w') as file:
            json.dump(data_to_save, file)

    def load(self, filename):
        with open(filename, 'r') as file:
            data_from_file = json.load(file)
            self._data = [DateTime.from_string(item) for item in data_from_file]
