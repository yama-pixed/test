class OrderSystem:
    def __init__(self):
        self.menu = {
            '1': {'item': 'Pizza', 'price': 10.99},
            '2': {'item': 'Burger', 'price': 5.99},
            '3': {'item': 'dal bhat', 'price': 3.99},
            '4': {'item': 'Ice Cream', 'price': 2.99},
            '5': {'item': 'MoMo','price':4.99}
        }
        self.cart = []

    def display_menu(self):
        print("===== Menu =====")
        for key, value in self.menu.items():
            print(f"{key}. {value['item']} - ${value['price']:.2f}")
        print("================")

    def take_order(self):
        print("Welcome to our ordering system!")
        while True:
            self.display_menu()
            choice = input("Enter the item number you want to order (or 'done' to finish): ")
            
            if choice.lower() == 'done':
                break

            if choice in self.menu:
                item = self.menu[choice]
                self.cart.append(item)
                print(f"{item['item']} added to your cart.")
            else:
                print("Invalid choice. Please select a valid item.")

    def show_order_summary(self):
        print("\n===== Order Summary =====")
        total_cost = sum(item['price'] for item in self.cart)
        for item in self.cart:
            print(f"{item['item']} - ${item['price']:.2f}")
        print("=========================")
        print(f"Total: ${total_cost:.2f}")
        print("=========================")

    def place_order(self):
        self.take_order()
        if self.cart:
            print("\nThank you for your order!")
            self.show_order_summary()
        else:
            print("No items in your order. Have a great day!")

if __name__ == "__main__":
    order_system = OrderSystem()
    order_system.place_order()
