# Create an empty list to store products
products = []
while True:
    print("\nMenu:")
    print("1. Product List")
    print("2. Add Product")
    print("3. Delete Product by Name")
    print("4. Delete Product by Index")
    print("5. Exit")

    # Ask for user input
    choice = input("Please input menu: ")

    # Option 1: Product List
    if choice == '1':
        if not products:
            print("No products available.")
        else:
            print("Product List:")
            for index, product in enumerate(products, start=1):
                print(f"{index}. {product}")

    # Option 2: Add Product
    elif choice == '2':
        name = input("Enter product name: ")
        products.append(name)
        print("Product added successfully.")

    # Option 3: Delete Product by Name
    elif choice == '3':
        name_to_delete = input("Enter the name of the product to delete: ")
        if name_to_delete in products:
            products.remove(name_to_delete)
            print(f"{name_to_delete} deleted successfully.")
        else:
            print("Product not found.")

    # Option 4: Delete Product by Index
    elif choice == '4':
        try:
            index_to_delete = int(input("Enter the index of the product to delete: "))
            if 1 <= index_to_delete <= len(products):
                del products[index_to_delete - 1]
                print("Product deleted successfully.")
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Option 5: Exit
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
