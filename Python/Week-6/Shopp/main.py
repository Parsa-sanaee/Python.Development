import json

class Store:
    def __init__(self, file_path):
        self.file_path = file_path
        self.products = self.load_database()

    def load_database(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_database(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.products, file, indent=4)
        except IOError as e:
            print(f"Error saving database: {e}")

    def add_product(self, product):
        self.products.append(product)
        self.save_database()
        print("Product added successfully.")

    def find_product(self, product_name):
        for product in self.products:
            if product["name"] == product_name:
                return product
        return None

    def delete_product(self, product_name):
        for i, product in enumerate(self.products):
            if product["name"] == product_name:
                del self.products[i]
                self.save_database()
                print(f"Product '{product_name}' deleted successfully.")
                return
        print(f"Product '{product_name}' not found.")

    def update_product(self, product_name, updated_info):
        for product in self.products:
            if product["name"] == product_name:
                product.update(updated_info)
                self.save_database()
                print(f"Product '{product_name}' information updated successfully.")
                return
        print(f"Product '{product_name}' not found.")

def get_product_input():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    brand = input("Enter product brand: ")
    return {"name": name, "price": price, "brand": brand}

def main():
    store = Store("products.json")
    print("Database loaded successfully.")

    while True:
        print("\nOptions:")
        print("1. Add product")
        print("2. Find product")
        print("3. Delete product")
        print("4. Update product")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            product = get_product_input()
            store.add_product(product)
        elif choice == '2':
            product_name = input("Enter product name to find: ")
            product = store.find_product(product_name)
            if product:
                print("Product found:")
                print(json.dumps(product, indent=4))
            else:
                print(f"Product '{product_name}' not found.")
        elif choice == '3':
            product_name = input("Enter product name to delete: ")
            store.delete_product(product_name)
        elif choice == '4':
            product_name = input("Enter product name to update: ")
            updated_info = {}
            updated_info["name"] = input("Enter new name (leave blank to keep current): ") or None
            updated_info["price"] = input("Enter new price (leave blank to keep current): ") or None
            updated_info["brand"] = input("Enter new brand (leave blank to keep current): ") or None
            updated_info = {k: v for k, v in updated_info.items() if v is not None}
            store.update_product(product_name, updated_info)
        elif choice == '5':
            store.save_database()
            print("Database saved successfully. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
