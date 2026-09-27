from ..shop.pricing import with_tax
from .mock_gateway import MockGateway


def checkout(order, region="pk"):
    total = with_tax(order.total(), region)
    MockGateway().charge(total)
    return total
