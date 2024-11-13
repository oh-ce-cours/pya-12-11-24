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
    return [Fruit("banana"), my_fruit("apple")]


def test_my_fruit_in_basket():
    # arange
    my_fruit = my_fruit()
    fruit_basket = fruit_basket()
    assert my_fruit in fruit_basket
