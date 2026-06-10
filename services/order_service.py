from models.product import Product
from models.order import Order

from utils.file_handler import read_data, write_data, append_data

# CSV Files 
PRODUCT_FILE = "data/products.csv"
ORDER_FILE = "data/orders.csv"

class OrderService:
    def load_products(self):
        products = []
        rows = read_data(PRODUCT_FILE)

        for row in rows:
            try:
                product_id = row[0]
                name = row[1]
                brand = row[2]
                cpu = row[3]
                ram = int(row[4])
                storage = int(row[5])   
                price = float(row[6])
                stock = int(row[7])

                products.append(
                    Product(product_id, name, brand, cpu, ram, storage, price, stock)
                )

            except (IndexError, ValueError): #IndexError for missing fields and ValueError for invalid data types
                print(f"Skipping invalid product row: {row}")

        return products
    def add_product(self):
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        brand = input("Enter Product Brand: ")
        cpu = input("Enter Product CPU: ")

        try:
            ram = int(input("Enter Product RAM(GB): "))
            storage = int(input("Enter Product Storage(GB): "))
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))

        except ValueError:
            print("Invalid input. Price must be number and stock must be integer.")
            return

        append_data(
            PRODUCT_FILE,
            ["id", "name", "brand", "cpu", "ram", "storage", "price", "stock"],
            [product_id, name, brand, cpu, ram, storage, price, stock]
        )

        print("\n--> Product added successfully... ✅")
    def delete_product(self):
        products = self.load_products()
        
        if len(products) == 0:
            print("No product found ❗️")
            return
        
        print("> Available product in stock 📥: ")
        for product in products:
            print(product)
            
        product_id = input("\n Enter product ID ot delete: ")
        
        select_product = None
        for product in products:
            if product.product_id == product_id:
                selected_product = product 
                break
            
        if selected_product is None:
            print("\n=== Product not found ❗️ ===")
            return
        
        confirm = input(f"Are you sure you want to delete {selected_product.name}? (yes/no): ").strip().lower()
        if confirm.lower() == "yes":
            products.remove(selected_product)
            write_data(
                PRODUCT_FILE,
                ["id", "name", "brand", "cpu", "ram", "storage", "price", "stock"],
                [[p.product_id, p.name, p.brand, p.cpu, p.ram, p.storage, p.price, p.stock] for p in products]
            )
            print(f"\n=== {selected_product.name} deleted successfully... ✅ ===")
        else:
            print("\n> Deletion cancelled...❗️")
    def view_stock(self):
        products = self.load_products()
        print("> PRODUCT AVAILABLE IN STOCK 📥\n")

        if len(products) == 0: #check if there are products in stock
            print("No products found ❗️")
            return

        for product in products:
            print(product) 
    def order_product(self):
        products = self.load_products()

        if len(products) == 0:
            print("No products available in stock❗️")
            return

        print("> AVAILABLE PRODUCTS IN STOCK 📥\n")
        print("ID | Name | Price | Stock")

        for product in products:
            print(product)

        customer_name = input("\nEnter Customer Name: ")
        product_id = input("Enter Product ID: ")

        try:
            phone_number = int(input("Enter Phone Number(+855): "))
            quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("Quantity must be an integer.")
            return

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
        # Find selected product
        selected_product = None

        # Find product
        for product in products:
            if product.product_id == product_id:
                selected_product = product
                break

        if selected_product is None:
            print("\n=== Product not found ❗️ ===")
            print("> Please check the product ID below:___🔍\n")
            
            for product in products:
                print(product)
            return

        # Check stock
        if quantity > selected_product.stock:
            print("\n=== Not enough stock ❗️ ===")
            print(f"> Available stock: {selected_product.stock} 📌")
            return

        # Calculate total
        total_price = quantity * selected_product.price

        # Generate order ID
        order_id = len(read_data(ORDER_FILE)) + 1

        # Create order object
        order = Order(order_id, customer_name, phone_number, selected_product.name, quantity, total_price)
        
        # Save order
        append_data(
                ORDER_FILE,
                ["id", "customer", "phone_number", "product", "quantity", "total_price"],
                [ order.order_id, order.customer_name, order.phone_number, order.product_name, order.quantity, order.total_price ]
            )

        # Update stock
        selected_product.stock -= quantity

        updated_products = []

        for product in products:
            updated_products.append([ product.product_id, product.name, product.brand, product.cpu, product.ram, product.storage, product.price, product.stock ])

        write_data(
            PRODUCT_FILE,
            ["id", "name", "brand", "cpu", "ram", "storage", "price", "stock"],
            updated_products
        )
        print("\n=== Order Successful✅ ===")
        print("> Invoice generated... 🧾")
        
        return order

    def invoice_order(self):
        rows = read_data(ORDER_FILE)
        print("> INVOICE ORDERS 🧾 :\n")

        if len(rows) == 0:
            print("No orders 📤")
            return

        for row in rows:
            try:
                order = Order(row[0], row[1], int(row[2]), row[3], int(row[4]), float(row[5]))
                print("-" * 30)
                print(order)
            except (IndexError, ValueError):
                print(f"Skipping invalid order row: {row}")