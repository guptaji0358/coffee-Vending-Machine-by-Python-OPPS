class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def refill(self, refill_type):
        """Refills the resources, returns approximate cost."""
        if refill_type == "half":
            amount = 100
        elif refill_type == "full":
            amount = 1000
        else:
            print("Invalid refill type. Choose 'half' or 'full'.")
            return 0

        for item in self.resources:
            self.resources[item] += amount

        # Simple cost calculation: $1 per unit for each resource
        cost = amount * len(self.resources)
        return cost
