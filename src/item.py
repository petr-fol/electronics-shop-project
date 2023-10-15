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
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if 0 < len(new_name) < 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, shell):
        with open(shell) as csv_f:
            csv_object = csv.DictReader(csv_f)
            list_items = []
            for row in csv_object:
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                item = cls(name, float(price), int(quantity))
                list_items.append(item)
        return list_items

    @staticmethod
    def string_to_number(num_str):
        if "." in num_str:
            int_num = ''
            for i in num_str:
                if i != ".":
                   int_num += i
                else:
                    break
            return int(int_num)
        else:
            return int(num_str)
