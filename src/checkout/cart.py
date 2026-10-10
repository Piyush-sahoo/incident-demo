"""Cart model for checkout-service."""
from dataclasses import dataclass, field


@dataclass
class LineItem:
    sku: str
    qty: int
    unit_price_cents: int


@dataclass
class Cart:
    cart_id: str
    items: list[LineItem] = field(default_factory=list)
    # v42 made coupons optional: carts without a coupon omit the key entirely.
    meta: dict = field(default_factory=dict)

    def subtotal_cents(self) -> int:
        return sum(i.qty * i.unit_price_cents for i in self.items)
