import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.pay_rate = pay_rate
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * Item.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self) -> str:
        """
        Возвращает название товара.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        """
        Устанавливает новое название товара.

        :param new_name: Новое название товара.
        """
        if 0 < len(new_name) < 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, link) -> None:
        """
        Создает экземпляры класса Item на основе данных из CSV-файла.

        :param link: Путь на CSV-файл с данными о товарах.
        """
        Item.all = []
        with open(link) as csv_f:
            csv_object = csv.DictReader(csv_f)
            list_items = []
            for row in csv_object:
                name = row['name']           # str
                price = row['price']         # str
                quantity = row['quantity']   # str
                item = cls(name, float(price), int(quantity))
                list_items.append(item)

    @staticmethod
    def string_to_number(num_str) -> int:
        """
        Преобразует строку, содержащую число, в число int типа.

        :param num_str: Строка, являющиеся числом.
        :return: Число int типа.
        """
        if "." in num_str:
            int_num = ''
            for i in num_str:
                if i != ".":
                    int_num += i
                else:
                    break
            return int(int_num)
        return int(num_str)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', price={self.price}, quantity={self.quantity})"

    def __str__(self) -> str:
        return f"Item: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def __add__(self, other) -> int:
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return None
