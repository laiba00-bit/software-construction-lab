def calculate_items_subtotal(order: dict) -> float:
    total = 0.0

    for item in order["items"]:
        price = item["price"]
        quantity = item["qty"]

        if price <= 0:
            continue

        if quantity <= 0:
            continue

        total = total + price * quantity

    return total


def calculate_member_discount(total: float, is_member: bool) -> float:
    if not is_member:
        return 0.0

    if total > 100:
        return total * 0.2

    if total > 50:
        return total * 0.1

    return 0.0


def calculate_shipping_cost(country: str) -> int:
    if country == "PK":
        return 5

    if country == "US":
        return 15

    return 25


def calculate_order_total(order: dict) -> float:
    subtotal = calculate_items_subtotal(order)
    discount = calculate_member_discount(subtotal, order["member"])
    shipping = calculate_shipping_cost(order["country"])

    total = subtotal - discount + shipping
    return total