import csv
import random
from tabulate import tabulate


def read_menu_from_csv(filename):
    """Reads the menu items and prices from a CSV file.

    Args:
        filename: The path to the CSV file.

    Returns:
        A dictionary mapping item names to their prices.
    """

    menu = {}
    try:
        with open(filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item_name = row["Item"]
                price = float(row["Price"])
                menu[item_name] = price
    except (FileNotFoundError, csv.Error) as e:
        print(f"Error reading menu file: {e}")
        raise
    return menu


def print_menu(menu):
    """Prints the menu in a readable format using tabulate.

    Args:
        menu: A dictionary mapping item names to their prices.
    """

    menu_headers = ["Item", "Price"]
    menu_items = [[item, f"${price:.2f}"] for item, price in menu.items()]
    print(tabulate(menu_items, headers=menu_headers, tablefmt="grid"))


def take_order(menu):
    """Takes an order from the user, collecting and validating item choices.

    Args:
        menu: A dictionary mapping item names to their prices.

    Returns:
        A list of ordered items or None if the user cancels the order.
    """

    order = []
    while True:
        item_name = input("Enter an item name (or 'End' to finish): ").strip().title()
        if item_name == "End":
            break

        if item_name not in menu:
            print("Item is not in the menu. Please try again.")
            continue
        while True:
            try:
                quantity = int(input(f"Enter quantity for '{item_name}': ").strip())
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                for _ in range(quantity):
                    order.append(item_name)
                break
            except ValueError:
                print("Quantity must be integer")
    return order if order else None


def calculate_total_price(order, menu):
    """Calculates the total price of the order.

    Args:
        order: A list of ordered items.
        menu: A dictionary mapping item names to their prices.

    Returns:
        The total price of the order.
    """

    total_price = 0.0
    for item_name in order:
        price = menu[item_name]
        total_price += price

    return total_price


def submit_order(order, total_price):
    """Submits the order by generating a random order number and writing it to a CSV file.

    Args:
        order: A list of ordered items.
        total_price: The total price of the order.
    """

    order_number = random.randint(100000, 999999)
    try:
        with open("order_history.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([order_number, ", ".join(order), f"${total_price:.2f}"])
        print(f"Your order ({order_number}) confirmed! Total price: ${total_price:.2f}")
    except csv.Error as e:
        print(f"Error writing order to file: {e}")


def remove_duplicates_preserving_count(data):
    """
    Returns a new list containing unique elements from the input list,
    formatted as "count element" (or just "element" if count is 1),
    preserving the exact number of occurrences and adding an 's' for plural forms.

    Args:
        data: A list of elements.

    Returns:
        A new list with formatted string representations of unique elements
        and their counts.
    """

    counts = {}  # Dictionary to store element counts
    unique_list = []  # List of unique elements

    for item in data:
        if item not in counts:  # First occurrence
            counts[item] = 1
            unique_list.append(item)
        else:  # Subsequent occurrences
            counts[item] += 1

    # Create formatted strings with counts and pluralization
    result = []
    for item in unique_list:
        count = counts[item]
        if count > 1:
            result.append(f"{count} {item}" + ("s" if count > 1 else ""))
        else:
            result.append(item)

    return result


def main():
    """The main function to run the program."""

    menu = read_menu_from_csv("menu.csv")
    print_menu(menu)  # Print the menu using tabulate
    order = take_order(menu)
    if order:
        total_price = calculate_total_price(order, menu)
        formatted_order = remove_duplicates_preserving_count(order)
        submit_order(formatted_order, total_price)


if __name__ == "__main__":
    main()
