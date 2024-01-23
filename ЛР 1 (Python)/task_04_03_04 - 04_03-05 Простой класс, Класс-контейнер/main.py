# Программирование на языке высокого уровня (Python).
# Задание №4.3.4. - 4.3.5 Вариант 5
#
# Выполнила: Гоморина А.В.
# Группа: ПИН-б-о-21-1
# E-mail: nastyagomorinalove@gmail.com


from DateTime import DateTime
from DateTimeCollection import DateTimeCollection

if __name__ == "__main__":
    # Создание объекта DateTime
    dt1 = DateTime(2022, 1, 16, 12, 30, 0)
    print("DateTime 1:", dt1)

    # Сложение и вычитание
    dt2 = DateTime(2022, 1, 17, 15, 45, 0)
    result_add = dt1 + dt2
    result_sub = dt1 - dt2
    print("Sum:", result_add)
    print("Difference:", result_sub)

    # Создание объекта из строки
    dt_str = "2022-01-18 08:00:00"
    dt_from_str = DateTime.from_string(dt_str)
    print("Создание DateTime из строки:", dt_from_str)

    # Сохранение и загрузка из файла
    dt1.save("datetime.json")
    dt_loaded = DateTime(1, 1, 1)
    dt_loaded.load("datetime.json")
    print("Загруженный DateTime:", dt_loaded)

    # Доступ к полям через свойства
    print("Year:", dt1.year)
    print("Month:", dt1.month)
    print("Day:", dt1.day)

    # 4.3.5
    # Создание контейнера и добавление объектов
    container = DateTimeCollection()
    container.add(dt1)
    container.add(dt2)

    # Вывод содержимого контейнера
    print("Контейнер:", container)

    # Сохранение контейнера в файл
    container.save("container.json")

    # Удаление элемента из контейнера
    container.remove(0)

    # Загрузка контейнера из файла
    container.load("container.json")

    # Вывод обновленного содержимого контейнера
    print("Вывод обновлённого контейнера:", container)
