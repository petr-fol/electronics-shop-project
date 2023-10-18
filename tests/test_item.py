"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

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
    items = Item.instantiate_from_csv('../src/items.csv')

    # assert len(items) == 3  # Проверяем количество созданных объектов Item

    item1 = Item.all[0]
    assert item1.name == "Смартфон"
    assert item1.price == 100.0
    assert item1.quantity == 1

    item2 = items[1]
    assert item2.name == "Ноутбук"
    assert item2.price == 1000
    assert item2.quantity == 3

    item3 = items[2]
    assert item3.name == "Кабель"
    assert item3.price == 10.0
    assert item3.quantity == 5


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


if __name__ == "__main__":
    pytest.main()
