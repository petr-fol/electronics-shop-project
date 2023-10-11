class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate_ = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int, pay_rate=1.0) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.pay_rate = pay_rate

    def calculate_total_price(self, pay_rate_) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.pay_rate = pay_rate_
        return self.price * self.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
