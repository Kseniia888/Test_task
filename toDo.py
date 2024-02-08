import json


class toDo:
    def __init__(self): #-> None:
        pass

    def get_product_names(file_path):

        with open(file_path, 'r') as file:

            data = json.load(file)

            product_names = [recepie.get('name') for recepie in data.get('products', [])]

            return product_names
    
    def suitible_products (file_path, price_threshold):

        with open(file_path, 'r') as file:
            data = json.load(file)
            suitible_products = [product for product in data.get('products', []) if product.get('price', 0) >= price_threshold]

        return suitible_products


    