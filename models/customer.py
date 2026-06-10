class Customer:

    def __init__(self, customer_id, name, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"Customer ID: {self.customer_id} | Customer Name: {self.name} | Phone Number: (+855) {self.phone_number}"
    