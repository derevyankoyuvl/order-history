# Ordering Food and Saving record to the History
#### Video Demo:  <https://youtu.be/mbB0a5ZMiRk>
#### Description:
This is program is created to provide ability for user to read Menu, select item from menu and choose quantity of it. User can add multiple items to an order. 
When user finishes addign items - he need to enter 'End' to finish ordering 
Submit Order will calculate order total based on selected items and quantity of the items

## Main
- Read Menu using `read_menu_from_csv(filename)`
- Print Menu using `print_menu(menu)`
- Select item and item's quantity using `take_order(menu)`
- Calculate Total Price using `calculate_total_price(order, menu)`
- Submit order using  `submit_order(order, total_price)`
- Remove duplicate items in the selected list of items `remove_duplicates_preserving_count(order)`


## Functions
- `read_menu_from_csv(filename)` read Menu using
- `print_menu(menu)` print Menu using
- `take_order(menu)` select item and item's quantity using
- `calculate_total_price(order, menu)` calculate Total Price using
- `submit_order(order, total_price)` submit order using
- `remove_duplicates_preserving_count(order)` remove duplicate items in the selected list of items

## Authors

- [@derevyankoyuvl](https://github.com/derevyankoyuvl)

## Prerequisites 
Check requirements.txt to install packages: 
```bash
  pip install csv
  pip install tabulate
```

## Running Tests

To run tests, run the following command

```bash
  pytest test_project.py
```

## Lessons Learned

I learned how to make a proper github repo, with README, and requirements files.
Applied knowledge I got diring CS50p course
