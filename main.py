from toDo import toDo
import json

def main():

    file_path = 'Recepies.json'  
    product_names = toDo.get_product_names(file_path)
    print("Product Names:", product_names) 

    price_threshold = float(input('Please type max price '))
    filtered_products = toDo.suitible_products(file_path, price_threshold)
    print(filtered_products)


if __name__ == "__main__":
    main()