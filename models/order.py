class Order:

    def __init__(self, order_id, customer_name, phone_number, product_name, quantity, total_price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.product_name = product_name
        self.quantity = quantity
        self.total_price = total_price
        
    def __str__(self):
        return (
            f"Order ID: {self.order_id}\n"
            f"Customer: {self.customer_name}\n"
            f"Phone Number: (+855) {self.phone_number}\n"
            f"Product: {self.product_name}\n"
            f"Quantity: {self.quantity}\n"
            f"Total Price: ${self.total_price:.2f}"
        )