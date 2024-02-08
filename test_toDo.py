import json
import pytest
from toDo import toDo


def test_get_product_names():

    file_path = 'Recepies.json' 
    expected_product_names = ["Pizza", "Sushi", "Burger", "Pad Thai"]
    assert toDo.get_product_names(file_path) == expected_product_names

def test_suitible_products():
    file_path = 'Recepies.json'
    price_threshold = 15
    expected_filtered_products = [
        {'id': 2, 'name': 'Sushi', 'category': 'Japanese', 'price': 24.99}
    ]
    assert toDo.suitible_products(file_path, price_threshold) == expected_filtered_products