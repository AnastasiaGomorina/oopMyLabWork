# Программирование на языке высокого уровня (Python).
# Задание №4.3.3. Вариант 5
#
# Выполнила: Гоморина А.В.
# Группа: ПИН-б-о-21-1
# E-mail: nastyagomorinalove@gmail.com


class TimeDeposit:
    """Абстрактный класс - срочный вклад.

    https://ru.wikipedia.org/wiki/Срочный_вклад.

    Поля:
      - self.name (str): наименование;
      - self._interest_rate (float): процент по вкладу (0; 100];
      - self._period_limit (tuple (int, int)):
            допустимый срок вклада в месяцах [от; до);
      - self._sum_limit (tuple (float, float)):
            допустимая сумма вклада [от; до).
    Свойства:
      - self.currency (str): знак/наименование валюты.
    Методы:
      - self._check_self(initial_sum, period): проверяет соответствие данных
            ограничениям вклада;
      - self.get_profit(initial_sum, period): возвращает прибыль по вкладу;
      - self.get_sum(initial_sum, period):
            возвращает сумму по окончании вклада.
    """

    def __init__(self, name, interest_rate, period_limit, sum_limit):
        """Инициализировать атрибуты класса."""
        self.name = name
        self._interest_rate = interest_rate
        self._period_limit = period_limit
        self._sum_limit = sum_limit

        # Проверить значения
        self._check_self()


    @property
    def __str__(self):
        """Вернуть строкое представление депозита.

        Формат вывода:

        Наименование:       Срочный Вклад
        Валюта:             руб.
        Процентная ставка:  5
        Срок (мес.):        [6; 18)
        Сумма:              [1,000; 100,000)
        """
        return (f"Наименование:       {self.name}\n"
                f"Валюта:             {self.currency}\n"
                f"Процентная ставка:  {self._interest_rate}\n"
                f"Срок (мес.):        [{self._period_limit[0]}; {self._period_limit[1]})\n"
                f"Сумма:              [{self._sum_limit[0]:,.0f}; {self._sum_limit[1]:,.0f})")

    @property
    def currency(self):
        return "руб."  # Не изменяется

    def _check_self(self):
        """Проверить, что данные депозита являются допустимыми."""
        assert 0 < self._interest_rate <= 100, \
            "Неверно указан процент по вкладу!"
        assert 1 <= self._period_limit[0] < self._period_limit[1], \
            "Неверно указаны ограничения по сроку вклада!"
        assert 0 < self._sum_limit[0] <= self._sum_limit[1], \
            "Неверно указаны ограничения по сумме вклада!"

    def _check_user_params(self, initial_sum, period):
        """Проверить, что данные депозита соответствуют его ограничениям."""
        is_sum_ok = self._sum_limit[0] <= initial_sum <= self._sum_limit[1]
        is_period_ok = self._period_limit[0] <= period < self._period_limit[1]
        assert is_sum_ok and is_period_ok, "Условия вклада не соблюдены!"

    def get_profit(self, initial_sum, period):
        """Вернуть прибыль по вкладу вклада клиента.

        Параметры:
          - initial_sum (float): первоначальная сумма;
          - period (int): количество месяцев размещения вклада.

        Формула:
          первоначальная_сумма * % / 100 * период / 12
        """
        # Проверить, укладывается ли вклад в ограничения
        self._check_user_params(initial_sum, period)
        # Выполнить расчет
        return initial_sum * self._interest_rate / 100 * period / 12

    def get_sum(self, initial_sum, period):
        """Вернуть сумму вклада клиента после начисления прибыли.

        Параметры:
          - initial_sum (float): первоначальная сумма;
          - period (int): количество месяцев размещения вклада.
        """
        # Проверить, укладывается ли вклад в ограничения
        return initial_sum + self.get_profit(initial_sum, period)


class BonusTimeDeposit(TimeDeposit):
    """Cрочный вклад c получением бонуса к концу срока вклада.

    Бонус начисляется как % от прибыли, если вклад больше определенной суммы.

    Атрибуты:
      - self._bonus (dict ("percent"=int, "sum"=float)):
        % от прибыли, мин. сумма;
    """

    def __init__(self, name, interest_rate, period_limit, sum_limit, bonus):
        """Инициализировать атрибуты класса."""
        self._bonus = bonus

        super().__init__(name, interest_rate, period_limit, sum_limit)

    def __str__(self):
        """Вернуть строкое представление депозита.

        К информации о родителе добавляется информацию о бонусе.

        Формат вывода:

        Наименование:       Бонусный Вклад
        Валюта:             руб.
        Процентная ставка:  5
        Срок (мес.):        [6; 18)
        Сумма:              [1,000; 100,000)
        Бонус (%):          5
        Бонус (мин. сумма): 2,000
        """
        parent_str = super().__str__
        bonus_str = (f"Бонус (%):          {self._bonus['percent']}\n"
                     f"Бонус (мин. сумма): {self._bonus['sum']:,.0f}")
        return f"{parent_str}\n{bonus_str}"

    def _check_self(self):
        """Проверить, что данные депозита являются допустимыми.

        Дополняем родительский метод проверкой бонуса.
        """
        super()._check_self()
        assert 0 < self._bonus['percent'] <= 100, "Неверно указан процент бонуса!"
        assert self._bonus['sum'] > 0, "Неверно указана минимальная сумма для бонуса!"

    def get_profit(self, initial_sum, period):
        """Вернуть прибыль по вкладу вклада клиента.

        Параметры:
          - initial_sum (float): первоначальная сумма;
          - period (int): количество месяцев размещения вклада.

        Формула:
          - прибыль = сумма * процент / 100 * период / 12

        Для подсчета прибыли используется родительский метод.
        Далее, если первоначальная сумма > необходимой,
        начисляется бонус.
        """
        self._check_user_params(initial_sum, period)

        # Выполнить расчет прибыли
        base_profit = super().get_profit(initial_sum, period)

        # Если первоначальная сумма больше минимальной для бонуса
        if initial_sum > self._bonus['sum']:
            bonus_amount = base_profit * self._bonus['percent'] / 100
            return base_profit + bonus_amount
        else:
            return base_profit


class CompoundTimeDeposit(TimeDeposit):
    """Cрочный вклад c ежемесячной капитализацией процентов."""

    def __str__(self):
        """Вернуть строкое представление депозита.

        К информации о родителе добавляется информация о капитализации.

        Формат вывода:

        Наименование:       Вклад с Капитализацией
        Валюта:             руб.
        Процентная ставка:  5
        Срок (мес.):        [6; 18)
        Сумма:              [1,000; 100,000)
        Капитализация %   : Да
        """
        parent_str = super().__str__
        return f"{parent_str}\nКапитализация %   : Да"

    def get_profit(self, initial_sum, period):
        """Вернуть прибыль по вкладу вклада клиента.

        Параметры:
          - initial_sum (float): первоначальная сумма;
          - period (int): количество месяцев размещения вклада.

        Родительский метод для подсчета прибыли использовать не нужно,
        переопределив его полностью - расчет осуществляется по новой формуле.
        Капитализация процентов осуществляется ежемесячно.

        Нужно не забыть про самостоятельный вызов проверки параметров.

        Формула:
          первоначальная_сумма * (1 + % / 100 / 12) ** период -
          первоначальная_сумма
        """
        self._check_user_params(initial_sum, period)

        # Выполнить расчет с учетом капитализации
        return initial_sum * ((1 + self._interest_rate / 100 / 12) ** period - 1)

# ---


deposits_data = dict(interest_rate=5, period_limit=(6, 18),
                     sum_limit=(1000, 100000))

# Список имеющихся депозитов
deposits = (
    TimeDeposit("Сохраняй", interest_rate=5,
                period_limit=(6, 18),
                sum_limit=(1000, 100000)),
    BonusTimeDeposit("Бонусный 2", **deposits_data,
                     bonus=dict(percent=5, sum=2000)),
    CompoundTimeDeposit("С капитализацией", **deposits_data),
    TimeDeposit("Еще один вклад", interest_rate=4,
                period_limit=(3, 12),
                sum_limit=(500, 50000)),
    BonusTimeDeposit("Еще один бонусный", interest_rate=6,
                     period_limit=(9, 24),
                     sum_limit=(2000, 80000),
                     bonus=dict(percent=7, sum=3000)),
    CompoundTimeDeposit("Еще один с капитализацией", interest_rate=5,
                        period_limit=(6, 18),
                        sum_limit=(2000, 150000))
)
