from store import *
import json

DATABASE_FILE = 'products.json'

def get_product_input():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    brand = input("Enter product brand: ")
    return {"name": name, "price": price, "brand": brand}

def main():
    products = load_database(DATABASE_FILE)
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
            add_product(products, product)
        elif choice == '2':
            product_name = input("Enter product name to find: ")
            product = find_product(products, product_name)
            if product:
                print("Product found:")
                print(json.dumps(product, indent=4))
            else:
                print(f"Product '{product_name}' not found.")
        elif choice == '3':
            product_name = input("Enter product name to delete: ")
            delete_product(products, product_name)
        elif choice == '4':
            product_name = input("Enter product name to update: ")
            updated_info = {}
            updated_info["name"] = input("Enter new name (leave blank to keep current): ") or None
            updated_info["price"] = input("Enter new price (leave blank to keep current): ") or None
            updated_info["brand"] = input("Enter new brand (leave blank to keep current): ") or None
            updated_info = {k: v for k, v in updated_info.items() if v is not None}
            update_product(products, product_name, updated_info)
        elif choice == '5':
            save_database(DATABASE_FILE, products)
            print("Database saved successfully. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
