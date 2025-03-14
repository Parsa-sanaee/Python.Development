import json

class Database:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_database()

    def load_database(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_database(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error saving database: {e}")

    def add_product(self, product):
        self.data.append(product)
        self.save_database()
        print("Product added successfully.")

    def find_product(self, product_name):
        for product in self.data:
            if product["name"] == product_name:
                return product
        return None

    def delete_product(self, product_name):
        for i, product in enumerate(self.data):
            if product["name"] == product_name:
                del self.data[i]
                self.save_database()
                print(f"Product '{product_name}' deleted successfully.")
                return
        print(f"Product '{product_name}' not found.")

    def update_product(self, product_name, updated_info):
        for product in self.data:
            if product["name"] == product_name:
                product.update(updated_info)
                self.save_database()
                print(f"Product '{product_name}' information updated successfully.")
                return
        print(f"Product '{product_name}' not found.")


db = Database("products.json")
db.add_product({"name": "Product1", "price": 100})
print(db.find_product("Product1"))
db.update_product("Product1", {"price": 150})
db.delete_product("Product1")
