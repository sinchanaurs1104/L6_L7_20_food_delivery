
import math


def parse_order(items_csv):
    if not isinstance(items_csv, str) or not items_csv.strip():
        raise ValueError("Order must be a non-empty string")

    order = {}

    for item in items_csv.split(','):
        parts = item.split(':')

        if len(parts) != 2:
            raise ValueError("Each item must have name:quantity format")

        name = parts[0].strip()
        qty = parts[1].strip()

        if not name:
            raise ValueError("Item name cannot be empty")

        try:
            quantity = int(qty)
        except (ValueError, TypeError):
            raise ValueError("Quantity must be an integer")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        order[name] = quantity

    return order


def delivery_eta(distance_km):
    try:
        distance = float(distance_km)
    except (ValueError, TypeError, OverflowError):
        raise ValueError("Distance must be a valid number")

    if not math.isfinite(distance) or distance < 0:
        raise ValueError("Distance must be finite and non-negative")

    return int(15 + distance * 4)


def coupon_discount(code):
    if not isinstance(code, str):
        raise ValueError("Coupon must be a string")

    code = code.strip().upper()

    if not code.startswith("SAVE"):
        raise ValueError("Invalid coupon format")

    discount = code[4:]

    if not discount or not discount.isascii() or not discount.isdigit():
        raise ValueError("Coupon must contain SAVE followed by digits")

    return int(discount)


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result)


if __name__ == "__main__":
    main()
