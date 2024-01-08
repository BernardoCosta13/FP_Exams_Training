from typing import Dict, Tuple

stock: Dict[str, Tuple[float, int]] = {
    "apples": (2.0, 10),
    "oranges": (1.5, 10),
    "milk": (3.0, 10),
    "water": (0.2, 10)
}

shopping_list: Dict[str, int] = {}

while True:
    item_name: str = input(
        "Enter the item name (or type 'done' to finish): ").lower()

    if item_name == 'done':
        break

    try:
        quantity: int = int(input("Enter the quantity: "))
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid quantity.")
        continue

    shopping_list[item_name] = quantity

total: float = 0.0
for item, quantity in shopping_list.items():
    price, available_quantity = stock.get(item, (0.0, 0))

    if available_quantity >= quantity:
        total += price * quantity
        updated_quantity = available_quantity - quantity
        stock[item] = (price, updated_quantity)
        print(f"Sold {quantity} {item}(s). Remaining stock: {updated_quantity}")
    else:
        print(
            f"Error: Insufficient stock for {item}. Available: {available_quantity}")

print(f"Total: {total:.2f} €")
