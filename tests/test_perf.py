import json
import pathlib

from src.shop.orders import Order


def test_big_orders_total():
    data = json.loads(pathlib.Path(__file__).with_name("fixtures").joinpath("big_orders.json").read_text())
    assert sum(Order(items).total() for items in data) == 160
