class Product:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.status = 'Unpurchased'

    def change_status(self):
        if self.status == 'Unpurchased':
            self.status = 'Purchased'
        else:
            self.status = 'Unpurchased'
        print(f"'{self.name}' status has been changed.")


class ProductsList:
    def __init__(self):
        self.products_list = []

    def add_product(self, name, amount):
        product = Product(name, amount)
        self.products_list.append(product)
        print(f"You add '{name}', amount: {amount}.")

    def display_list(self):
        if self.products_list.__len__() > 0:
            print("==== Products list ====")
            for product in self.products_list:
                print(f"Product: {product.name}, Amount: {product.amount}, Status: {product.status}")
            print("===================")
        else:
            print("You haven't added any products yet.")

    def change_status(self, name):
        product = self.find_product(name)
        if product:
            product.change_status()
        else:
            print(f"You haven't got '{name}' in your list.")

    def delete_product(self, name):
        product = self.find_product(name)
        if product:
            self.products_list.remove(product)
            print(f"'{name}' has been deleted")
        else:
            print(f"You haven't got '{name}' in your list.")

    def find_product(self, name):
        for product in self.products_list:
            if product.name.lower() == name.lower():
                return product
        return None


def main():
    products_list = ProductsList()

    while True:

        print("1. Add product")
        print("2. Display products list")
        print("3. Change product status")
        print("4. Delete product")
        print("5. Quit")
        menu_choice = input()

        if menu_choice == "1":
            name = input("Enter product name: ")
            amount = input(f"Enter amount of '{name}': ")
            products_list.add_product(name, amount)

        elif menu_choice == "2":
            products_list.display_list()

        elif menu_choice == "3":
            name = input("Enter product name you have bought: ")
            products_list.change_status(name)

        elif menu_choice == "4":
            name = input("Enter product name you want delete: ")
            products_list.delete_product(name)

        elif menu_choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid number! (1-5)")


if __name__ == '__main__':
    main()
