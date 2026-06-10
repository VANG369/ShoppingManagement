class Product:

    def __init__(self, product_id, name, brand, cpu, ram, storage, price, stock):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.cpu = cpu
        self.ram = int(ram)
        self.storage = int(storage)
        self.price = float(price)
        self.stock = int(stock)

    def __str__(self):
        return (
            f"Product ID: {self.product_id} | "
            f"Model: {self.name} | "
            f"Brand: {self.brand} | "
            f"CPU: {self.cpu} | "
            f"RAM: {self.ram}GB | "
            f"Storage: {self.storage}GB | "
            f"Price: $ {self.price:.2f} | "
            f"Stock: {self.stock}"
        )