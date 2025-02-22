import json

def load_database(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_database(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving database: {e}")

def add_product(products_list, product):
    products_list.append(product)
    print("Product added successfully.")

def find_product(products_list, product_name):
    for product in products_list:
        if product["name"] == product_name:
            return product
    return None

def delete_product(products_list, product_name):
    for i, product in enumerate(products_list):
        if product["name"] == product_name:
            del products_list[i]
            print(f"Product '{product_name}' deleted successfully.")
            return
    print(f"Product '{product_name}' not found.")

def update_product(products_list, product_name, updated_info):
    for product in products_list:
        if product["name"] == product_name:
            product.update(updated_info)
            print(f"Product '{product_name}' information updated successfully.")
            return
    print(f"Product '{product_name}' not found.")
