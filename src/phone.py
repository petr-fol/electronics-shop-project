from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_count: int) -> None:
        super().__init__(name, price, quantity)
        if sim_count <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.sim_count = sim_count

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_count})"
