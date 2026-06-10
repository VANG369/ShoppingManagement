from services.order_service import OrderService
from utils.display_menu import display_menu

service = OrderService()
# jijiu
while True:
    display_menu()
    choice = input("Enter choice(1-6): ")
    match choice:
        case "1":
            print("\n=== ADD PRODUCT TO STOCK 📦 ===")
            service.add_product()
        case "2":
            print("\n=== DELETE PRODUCTS 🗑️ ===")
            service.delete_product()
        case "3":
            print("\n=== VIEW STOCK PRODUCTS 📋 ===")
            service.view_stock()
        case "4":
            print("\n=== ORDER PRODUCT FROM STOCK 🛒 ===")
            service.order_product()
        case "5":
            print("\n=== INVOICE ORDER DETAILS 🧾 ===")
            service.invoice_order()
        case "6":
            print("\nThank You For Using Our Service!🙏")
            print("Exiting the system...\n")
            break
        case _:
            print("\n-> Invalid choice! Please try again...❗️")
