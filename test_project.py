import pytest
from tabulate import tabulate
import unittest
from unittest.mock import patch, mock_open

from project import (
    read_menu_from_csv,
    take_order,
    calculate_total_price
)

menu = {"Hamburger": 8.50, "Pizza": 9.95, "Sushi": 10.50}


class TestReadMenuFromCSV(unittest.TestCase):

    def test_read_actual_csv(self):
        # No need for mock data, use the actual file
        filename = "menu.csv"

        with open(filename, 'r') as csvfile:
            # Check if the file exists before proceeding
            if not csvfile:
                raise FileNotFoundError(f"Could not find file: {filename}")

            # Use the CSV file directly
            menu = read_menu_from_csv(filename)

            # Assert expected items and prices (adjust based on your data)
            self.assertEqual(menu["Hamburger"], 8.50)
            self.assertEqual(menu["French Fries"], 5.75)

    def test_read_empty_csv(self):
        with pytest.raises(TypeError):
            read_menu_from_csv()


class TestTakeOrder(unittest.TestCase):

    def test_valid_order(self):
        # Mock user input
        with patch(
            "builtins.input", side_effect=["Hamburger", "2", "Pizza", "1", "End"]
        ):
            # Call the function
            order = take_order(menu)

            # Assert the expected results
            self.assertEqual(order, ["Hamburger", "Hamburger", "Pizza"])

    def test_invalid_item(self):
        # Mock user input with invalid item
        with patch("builtins.input", side_effect=["End"]):
            # Expect no items in the order
            order = take_order(menu)
            self.assertEqual(order, None)

    def test_cancel_order(self):
        # Mock user input to cancel early
        with patch("builtins.input", side_effect=["End"]):
            # Expect no items in the order
            order = take_order(menu)
            self.assertIsNone(order)

    def test_mixed_valid_invalid(self):
        # Mock user input with mixed valid and invalid items
        with patch(
            "builtins.input",
            side_effect=["Hamburger", "2", "Sushi", "1", "Fries", "3", "End"],
        ):
            # Expect only valid items in the order
            order = take_order(menu)
            self.assertEqual(order, ["Hamburger", "Hamburger", "Sushi"])


class TestCalculateTotalPrice(unittest.TestCase):

    def test_empty_order(self):
        # Test with an empty order
        order = []
        expected_price = 0.0
        actual_price = calculate_total_price(order, menu)
        self.assertEqual(expected_price, actual_price)

    def test_single_item(self):
        # Test with a single item order
        order = ["Hamburger"]
        expected_price = menu["Hamburger"]
        actual_price = calculate_total_price(order, menu)
        self.assertEqual(expected_price, actual_price)

    def test_multiple_items(self):
        # Test with multiple items order
        order = ["Hamburger", "Pizza", "Sushi"]
        expected_price = menu["Hamburger"] + menu["Pizza"] + menu["Sushi"]
        actual_price = calculate_total_price(order, menu)
        self.assertEqual(expected_price, actual_price)

    def test_invalid_item(self):
        # Test with an order containing an invalid item
        order = ["Hamburger", "Fries", "Sushi"]
        with self.assertRaises(KeyError):
            calculate_total_price(order, menu)


if __name__ == "__main__":
    unittest.main()
