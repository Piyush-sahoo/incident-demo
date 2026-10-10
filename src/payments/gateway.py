"""Payments gateway client (payments-service)."""
import os

GATEWAY_URL = os.environ.get("PAYMENTS_GATEWAY_URL", "https://pay.example.internal")


def charge(cart_id: str, amount_cents: int) -> dict:
    if amount_cents <= 0:
        raise ValueError("amount must be positive")
    return {"cart_id": cart_id, "amount_cents": amount_cents, "status": "authorized"}
