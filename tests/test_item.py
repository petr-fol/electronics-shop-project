"""Здесь надо написать тесты с использованием pytest для модуля item."""
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

