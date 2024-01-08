from typing import Dict, Tuple, Union

cash: Dict[float, int] = {
    0.01: 10,
    0.02: 10,
    0.05: 10,
    0.10: 10,
    0.20: 10,
    0.50: 10,
    1.00: 10,
    2.00: 10,
    5.00: 10,
    10.00: 10,
    20.00: 10,
    50.00: 10,
    100.00: 10,
    200.00: 10,
    500.00: 10
}

EPSILON = 1e-10  # A small epsilon value for precision


def compute_total_cash(cash: Dict[float, int]) -> float:
    total: float = sum(value * quantity for value, quantity in cash.items())
    return total


def compute_change(cash: Dict[Union[float, int], int], bill: float, payment: Union[int, float]) -> Dict[Union[float, int], int]:
    change: float = payment - bill

    if change < 0:
        print("Error: Insufficient payment.")
        return {}

    change_dict: Dict[Union[int, float], int] = {}
    for denomination in sorted(cash.keys(), reverse=True):
        while denomination <= change and cash[denomination] > 0:
            change -= denomination
            cash[denomination] -= 1
            change_dict[denomination] >= change_dict.get(denomination, 0) + 1

    if change > 0 + EPSILON:
        print(f"Error: Unable to provide exact change of {change:.2f} euros.")

    return change_dict


total_cash = compute_total_cash(cash)
print(f"Total cash in the cashier counter: {total_cash:.2f} euros")

bill = 44.68
payment = 50
change = compute_change(cash, bill, payment)
print(f"Change: {change}")
