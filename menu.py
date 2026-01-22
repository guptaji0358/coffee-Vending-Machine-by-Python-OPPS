class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
            MenuItem(name="Espresso", water=30, milk=0, coffee=7, cost=2.5),
            MenuItem(name="Cappuccino", water=30, milk=120, coffee=7, cost=3.5),
            MenuItem(name="Latte", water=30, milk=200, coffee=7, cost=4.0),
            MenuItem(name="Dark Roast Espresso", water=30, milk=0, coffee=9, cost=3.0),
            MenuItem(name="Black Coffee", water=150, milk=0, coffee=10, cost=2.8),
            MenuItem(name="Light Roast Americano", water=120, milk=0, coffee=7, cost=3.0),
            MenuItem(name="Flat White", water=30, milk=150, coffee=7, cost=4.0),
            MenuItem(name="Sugar-Free Latte", water=30, milk=200, coffee=7, cost=4.2),
            MenuItem(name="Mocha", water=30, milk=150, coffee=7, cost=4.5),
            MenuItem(name="Macchiato", water=30, milk=20, coffee=7, cost=3.2),
            MenuItem(name="Turkish Coffee", water=60, milk=0, coffee=10, cost=3.0),
            MenuItem(name="Indian Filter Coffee", water=100, milk=100, coffee=10, cost=2.8),
            MenuItem(name="Café au Lait", water=60, milk=120, coffee=7, cost=3.5),
            MenuItem(name="Irish Coffee", water=60, milk=30, coffee=7, cost=6.0),
            MenuItem(name="Café Cubano", water=30, milk=0, coffee=7, cost=3.0),
            MenuItem(name="Vienna Coffee", water=60, milk=60, coffee=7, cost=4.0),
            MenuItem(name="Ristretto", water=20, milk=0, coffee=7, cost=2.5),
            MenuItem(name="Affogato", water=30, milk=0, coffee=7, cost=5.0),
            MenuItem(name="Cortado", water=30, milk=30, coffee=7, cost=3.5),
            MenuItem(name="Lungo", water=60, milk=0, coffee=7, cost=3.0),
            MenuItem(name="Red Eye", water=150, milk=0, coffee=14, cost=3.5),
            MenuItem(name="Mazagran", water=100, milk=0, coffee=10, cost=3.2),
            MenuItem(name="Bicerin", water=30, milk=60, coffee=7, cost=4.8),
            MenuItem(name="Kopi Tubruk", water=120, milk=0, coffee=12, cost=2.7),
            MenuItem(name="Café Bombón", water=30, milk=30, coffee=7, cost=3.5),
        ]

    def get_items(self):
        items = []
        for item in self.menu:
            items.append(item.name)
        return items

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
