from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    # Item.instantiate_from_csv('../src/items.csv')
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    # Item.instantiate_from_csv('../src/items_err.csv')
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден
