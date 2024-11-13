# https://docs.pytest.org/en/stable/explanation/fixtures.html
import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


def my_fruit():
    return Fruit("apple")


def fruit_basket():
    return [Fruit("banana"), my_fruit()]


def test_my_fruit_in_basket():
    # arange
    fruit = my_fruit()
    basket = fruit_basket()
    assert fruit in basket
