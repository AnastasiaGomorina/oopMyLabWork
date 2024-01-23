# Программирование на языке высокого уровня (Python).
# Задание №4.3.6. Вариант 5
#
# Выполнил: Гоморина А.В.
# Группа: ПИН-б-о-21-1
# E-mail: nastyagomorinalove@gmail.com

from Билет import Билет


class БезлимитныйБилет(Билет):
    def __init__(self):
        super().__init__(float('inf'))

    def информация(self):
        print("Это безлимитный билет.")