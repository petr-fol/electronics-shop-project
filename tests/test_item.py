"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.exeptions import InstantiateCSVError
from src.item import Item
from src.phone import Phone

test_item = Item("name", 1.0, 1)


def test_args():
    assert test_item.name == "name"
    assert test_item.price == 1.0
    assert test_item.quantity == 1
    price = test_item.calculate_total_price()
    assert test_item.pay_rate == 1.0
    assert price == 1.0


def test_calculate_total_price():
    price = test_item.calculate_total_price()
    assert price == 1.0
    assert type(price) == float


def test_apply_discount():
    test_item.apply_discount()
    assert test_item.price == 1.0


def test_name_property():
    item = Item("ShortName", 10.0, 5)
    assert item.name == "ShortName"
    assert item.price == 10.0
    assert item.quantity == 5

    item.name = "VeryLongNameThatExceedsTheLimit"
    assert item.name == "VeryLongNa"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')

    # assert len(items) == 3  # Проверяем количество созданных объектов Item

    item1 = Item.all[0]
    assert item1.name == "Смартфон"
    assert item1.price == 100.0
    assert item1.quantity == 1

    item2 = Item.all[1]
    assert item2.name == "Ноутбук"
    assert item2.price == 1000
    assert item2.quantity == 3

    item3 = Item.all[2]
    assert item3.name == "Кабель"
    assert item3.price == 10.0
    assert item3.quantity == 5


# test_instantiate_csv_error.py
def test_default_message():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("'../src/items_err.csv'")


def test_string_to_number():
    num_str = "123.45"
    assert Item.string_to_number(num_str) == 123

    num_str = "678"
    assert Item.string_to_number(num_str) == 678

    num_str = "9.876"
    assert Item.string_to_number(num_str) == 9

    num_str = "0"
    assert Item.string_to_number(num_str) == 0

    num_str = "-42.5"
    assert Item.string_to_number(num_str) == -42


# Тесты для метода __str__
def test_str_():
    item = Item("Ноутбук", 1500.0, 5)
    assert str(item) == "Item: Ноутбук, Price: 1500.0, Quantity: 5"


# Тесты для метода __repr__
def test_repr_():
    item = Item("Ноутбук", 1500.0, 5)
    assert repr(item) == "Item(name='Ноутбук', price=1500.0, quantity=5)"


def test_add_():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


if __name__ == "__main__":
    pytest.main()
