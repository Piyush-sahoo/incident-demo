"""Pricing for checkout-service.

v42: coupons became optional (cart.meta may not contain 'coupon_id').
"""
from .cart import Cart

COUPONS = {"WELCOME10": 0.10, "VIP25": 0.25}
TAX_RATE = 0.08


def discount_rate(cart: Cart) -> float:
    # BUG (v42): carts without a coupon no longer carry 'coupon_id' -> KeyError -> HTTP 500
    coupon = cart.meta["coupon_id"]
    return COUPONS.get(coupon, 0.0)


def total_cents(cart: Cart) -> int:
    subtotal = cart.subtotal_cents()
    discounted = subtotal * (1 - discount_rate(cart))
    return int(round(discounted * (1 + TAX_RATE)))
