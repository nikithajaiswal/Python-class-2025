class GroceryList:
    def __init__(self):
        self.items = {}
# Add a new item to the grocery list
    def add_item(self, name, quantity):
        if name in self.items:
            print(f"Item '{name}' already exists. Use 'update' to change quantity.")
        else:
            self.items[name] = quantity
            print(f"Added '{name}' with quantity {quantity}.")

# Remove an item by name
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Removed '{name}'.")
        else:
            print(f"Item '{name}' not found.")

# Update the quantity of an item
    def update_item(self, name, quantity):
        if name in self.items:
            self.items[name] = quantity
            print(f"Updated '{name}' quantity to {quantity}.")
        else:
            print(f"Item '{name}' not found.")

# Display the sorted list by item name
    def display_sorted_list(self):
        sorted_items = sorted(self.items.items())
        print("Sorted List:")
        for name, quantity in sorted_items:
            print(f"{name} - {quantity}")

# Display the total number of items
    def display_total_items(self):
        total = sum(self.items.values())
        print(f"Total items: {total}")


# Example usage:
# grocery_list = GroceryList()
# grocery_list.add_item("milk", 2)
# grocery_list.add_item("eggs", 12)
# grocery_list.update_item("milk", 3)
# grocery_list.remove_item("eggs")
# grocery_list.display_sorted_list()
# grocery_list.display_total_items()