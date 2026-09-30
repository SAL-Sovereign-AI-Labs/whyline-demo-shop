from ..shop.pricing import with_tax
from .gateway import Gateway


def checkout(order, region="pk"):
    total = with_tax(order.total(), region)
    Gateway().charge(total)
    return total
