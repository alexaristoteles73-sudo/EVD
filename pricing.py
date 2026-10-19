"""Indicative price rules taken from the QuickPrint business proposal.

These values have not been confirmed as current shop prices; visitors should verify them in person.
"""
from decimal import Decimal, InvalidOperation

SERVICE_RATES = {
    "bw-print": {
        "label": "Black-and-white printing",
        "rate": Decimal("1"),
        "rate_label": "₱1 per short-bond page",
        "kind": "page",
        "short_bond_only": True,
    },
    "color-print": {
        "label": "Color printing",
        "rate": Decimal("4"),
        "rate_label": "₱4 per short-bond page",
        "kind": "page",
        "short_bond_only": True,
    },
    "photocopy": {
        "label": "Photocopying",
        "rate": Decimal("5"),
        "rate_label": "₱5 per page",
        "kind": "page",
        "short_bond_only": True,
    },
    "lamination": {
        "label": "Lamination",
        "rate": Decimal("20"),
        "rate_label": "₱20 per item",
        "kind": "item",
        "short_bond_only": False,
    },
    "computer-station": {
        "label": "Computer station",
        "rate": Decimal("1"),
        "rate_label": "₱1 per 5 minutes",
        "kind": "minute",
        "short_bond_only": False,
    },
    "scanning": {
        "label": "Scanning",
        "rate": None,
        "rate_label": "Request a quote",
        "kind": "item",
        "short_bond_only": False,
    },
    "formatting": {
        "label": "Document formatting",
        "rate": None,
        "rate_label": "Request a quote",
        "kind": "item",
        "short_bond_only": False,
    },
    "binding": {
        "label": "Binding",
        "rate": None,
        "rate_label": "Request a quote",
        "kind": "item",
        "short_bond_only": False,
    },
}


def get_service(service_key):
    """Return one service definition, or None for a blank/unknown choice."""
    return SERVICE_RATES.get(service_key)


def calculate_total(service_key, quantity, copies=1, paper_size="short-bond"):
    """Calculate an indicative subtotal, or return None when a quote is needed.

    `quantity` is pages, items, or computer-station minutes. All numeric values must be
    positive whole numbers within practical limits.
    """
    service = get_service(service_key)
    if service is None:
        raise ValueError("Please choose a listed service.")

    try:
        quantity = int(quantity)
        copies = int(copies)
    except (TypeError, ValueError, InvalidOperation) as exc:
        raise ValueError("Enter a whole-number quantity and number of copies.") from exc

    if quantity < 1 or quantity > 10000:
        raise ValueError("Quantity must be between 1 and 10,000.")
    if copies < 1 or copies > 1000:
        raise ValueError("Number of copies must be between 1 and 1,000.")

    rate = service["rate"]
    if rate is None:
        return None
    if service["short_bond_only"] and paper_size != "short-bond":
        return None

    if service["kind"] == "page":
        units = quantity * copies
    elif service["kind"] == "minute":
        if quantity % 5 != 0:
            raise ValueError("Computer station time must be entered in 5-minute increments.")
        units = quantity // 5
    else:
        units = quantity

    return rate * Decimal(units)


def format_pesos(amount):
    """Format whole-peso and fractional estimates clearly."""
    if amount is None:
        return "Request a quote"
    amount = Decimal(amount)
    if amount == amount.to_integral_value():
        return f"₱{amount:,.0f}"
    return f"₱{amount:,.2f}"
