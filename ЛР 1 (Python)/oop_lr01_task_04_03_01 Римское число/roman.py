# Программирование на языке высокого уровня (Python).
# Задание №4.3.1. Вариант 5
#
# Выполнила: Гоморина А.В.
# Группа: ПИН-б-о-21-1
# E-mail: nastyagomorinalove@gmail.com


class Roman:
    """Класс Roman реализует работу с римскими числами.

    Алгоритм: http://math.hws.edu/eck/cs124/javanotes7/c8/ex3-ans.html.

    Внутри класс работает с обычными арабскими числами (int),
    которые преобразуются в римские при необходимости (например, при выводе).

    Ключевой атрибут: self._arabic (арабское число).

    Ограничения: число должно быть в пределах [1; 3999].
    """

    # Константы класса
    ARABIC_MIN = 1
    ARABIC_MAX = 3999
    ROMAN_MIN = "I"
    ROMAN_MAX = "MMMCMXCIX"

    LETTERS = ["M", "CM", "D", "CD", "C", "XC", "L",
               "XL", "X", "IX", "V", "IV", "I"]
    NUMBERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def __init__(self, value):
        """Инициализация класса.

        Параметры:
            value (str): римское число, например, X.
                или
            value (int): арабское число, например, 5.
                или
            value (другой тип):  возбудить исключение TypeError.
        """
        if not isinstance(value, (int, str)):
            raise TypeError("Не могу создать римское число из {0}".
                            format(type(value)))

        if isinstance(value, int):
            self.__check_arabic(value)
            self._arabic = value
        elif isinstance(value, str):
            self._arabic = self.to_arabic(value)

    def __add__(self, other):
        """Создать новый объект как сумму 'self' и 'other'.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, добавить к self.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        if isinstance(other, Roman):
            return Roman(self._arabic + other.arabic)
        elif isinstance(other, int):
            return Roman(self._arabic + other)
        else:
            raise TypeError("Неверный тип для сложения")

    def __sub__(self, other):
        """Создать новый объект как разность self и other.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, вычесть из self.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        if isinstance(other, Roman):
            return Roman(self._arabic - other.arabic)
        elif isinstance(other, int):
            return Roman(self._arabic - other)
        else:
            raise TypeError("Неверный тип для вычитания")

    def __mul__(self, other):
        """Создать новый объект как произведение self и other.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, умножить self на него.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        if isinstance(other, Roman):
            return Roman(self._arabic * other.arabic)
        elif isinstance(other, int):
            return Roman(self._arabic * other)
        else:
            raise TypeError("Неверный тип для умножения")

    def __floordiv__(self, other):
        """Создать новый объект как частное self и other.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, разделить self на него.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        if isinstance(other, Roman):
            return Roman(self._arabic // other.arabic)
        elif isinstance(other, int):
            return Roman(self._arabic // other)
        else:
            raise TypeError("Неверный тип для деления")

    def __truediv__(self, other):
        """Создать новый объект как частное self и other.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, разделить self на него.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        return self.__floordiv__(other)

    def __str__(self):
        """Вернуть строковое представление класса."""
        return Roman.to_roman(self._arabic)

    @staticmethod
    def __check_arabic(value):
        """Возбудить исключение ValueError, если 'value' не принадлежит
        [ARABIC_MIN; ARABIC_MIN]."""
        if not Roman.ARABIC_MIN <= value <= Roman.ARABIC_MAX:
            raise ValueError("Арабское число должно быть в пределах [{0}; {1}]".
                             format(Roman.ARABIC_MIN, Roman.ARABIC_MAX))

    @staticmethod
    def __check_roman(value):
        """Возбудить исключение ValueError, если 'value' содержит
        недопустимые символы (не входящие в LETTERS)."""
        if not all(char in Roman.LETTERS for char in value):
            raise ValueError("Римское число содержит недопустимые символы")

    @property
    def arabic(self):
        """Вернуть арабское представление числа."""
        return self._arabic

    @staticmethod
    def to_arabic(roman):
        """Преобразовать римское число 'roman' в арабское.

        Параметры:
            roman (str): римское число, например, "X".

        Возвращает:
            int: арабское число.
        """
        def letter_to_number(letter):
            """Вернуть арабское значение римской цифры 'letter'.

            Регистр не учитывается."""
            letter = letter.upper()
            return Roman.NUMBERS[Roman.LETTERS.index(letter)]

        Roman.__check_roman(roman)

        i = 0
        value = 0

        while i < len(roman):

            number = letter_to_number(roman[i])

            i += 1

            if i == len(roman):
                value += number
            else:
                next_number = letter_to_number(roman[i])
                if next_number > number:
                    value += next_number - number
                    i += 1
                else:
                    value += number

        Roman.__check_arabic(value)
        return value

    @staticmethod
    def to_roman(arabic):
        """Преобразовать арабское число 'arabic' в римское.

        Параметры:
            arabic (int): арабское число, например, 5.

        Возвращает:
            str: римское число.
        """
        Roman.__check_arabic(arabic)

        roman = ""
        n = arabic

        for i, number in enumerate(Roman.NUMBERS):
            while n >= number:
                roman += Roman.LETTERS[i]
                n -= Roman.NUMBERS[i]

        return roman
