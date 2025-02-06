products = [
    {"name": "Laptop", "price": 1200, "brand": "Asus"},
    {"name": "Mouse", "price": 25, "brand": "Logitech"},
    {"name": "Keyboard", "price": 75, "brand": "Corsair"},
]


def add_product(products_list):
    new_product = {}
    new_product["name"] = input("Enter product name: ")
    new_product["price"] = float(input("Enter product price: "))
    new_product["brand"] = input("Enter product brand: ")
    products_list.append(new_product)
    print("Product added successfully.")


def find_product(products_list, product_name):
    for product in products_list:
        if product["name"] == product_name:
            print("Product found:")
            print(product)
            return
    print(f"Product '{product_name}' not found.")


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


add_product(products)
find_product(products, "Mouse")
delete_product(products, "Keyboard")
update_product(products, "Laptop", {"price": 1300, "brand": "HP"})
print(products)