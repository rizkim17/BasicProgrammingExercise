
products = [
    {"name": "Skin Cleanser", "supplier_price": 23000, "stock": 10},
    {"name": "Oily Skin Cleanser", "supplier_price": 33000, "stock": 5},
    {"name": "Moisturizer SPF15", "supplier_price": 30000, "stock": 9},
    {"name": "Sunscreen Mexoryl", "supplier_price": 84000, "stock": 7},
    {"name": "Brightening Night", "supplier_price": 200000, "stock": 10},
    {"name": "Glow Daily Cream", "supplier_price": 180000, "stock": 7},
    {"name": "Activation Serum", "supplier_price": 120000, "stock": 9}
]
transactions = 0
total_profit = 0

def display_products():
    print("\n PRODUCT LISTS & PRICES : \n=======================================================================================")
    print("No.| Name\t\t\t\t| Supplier Price\t| Price to Sell\t| Stock\n=======================================================================================")
    for i, product in enumerate(products, start=1):
        print(f"{i}.   {product['name']}\t\t\t  Rp. {product['supplier_price']:,}\t\t  Rp. {int(product['supplier_price'] * 1.10):,}\t  {product['stock']}")
    print("=======================================================================================")

def transaction(product):
    global total_profit
    global transactions

    if product['stock'] == 0:
        print(f"{product['name']} is out of stock.\n")
    else:
        quantity = int(input("Quantity: "))
        if quantity > product['stock']:
            print(f"Insufficient stock. {product['stock']} {product['name']}s available.\n")
        else:
            product['stock'] -= quantity
            total = quantity * int(product['supplier_price'] * 1.10)
            total_profit += quantity * (product['supplier_price'] * 0.10)
            transactions += 1

            print(f"\n Selling {quantity} {product['name']}")
            print(f" Total \t\t\t: RP. {total:,}")
            display_products()
            print(f" Today transaction \t: {transactions}")
            print(f" Today Profit \t\t: RP. {total_profit:,}")
            print("=======================================================================================")


display_products()

while True:
    menu = input("Enter the purchased item (number) or 'exit' to complete the transaction: ")
    if menu.lower() == 'exit':
        print("\nThank you :)\n")
        break
    elif menu.isdigit() and 1 <= int(menu) <= len(products):
        transaction(products[int(menu) - 1])
    else:
        print("Invalid input. Please enter a valid item number or 'exit'.")
