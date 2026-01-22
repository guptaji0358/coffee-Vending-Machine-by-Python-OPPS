# import sys
from prettytable import PrettyTable

# raw_data_path = r"E:\Program Files\RobinData\WORK\RawData"
# sys.path.append(raw_data_path)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

on_off = True

while on_off:

    choice = input(
        "What you want to order? "
        "(type 'menu', 'report', 'refill', or 'off'): "
    )

    if choice == "off":
        on_off = False
        print("You Have Turned off the Machine")

    elif choice == "report":
        coffee_maker.report()
        print(f"Profit: ${money_machine.profit}")

    elif choice == "menu":
        table = PrettyTable()
        table.field_names = ["Available Coffee"]
        for item in menu.get_items():
            table.add_row([item])
        print(table)

    elif choice == "refill":
        refill_type = input("Do you want 'half' or 'full' refill? ").lower()
        cost = coffee_maker.refill(refill_type)
        remaining = money_machine.deduct_profit(cost)
        if remaining > 0:
            print(f"Profit is not enough. You need to pay ${remaining}")
            pay = float(input("Insert payment: "))
            if pay >= remaining:
                print("Thank you! Bonus +500ml coffee added!")
                coffee_maker.resources["coffee"] += 500
            else:
                print("Not enough payment. Refill incomplete.")
        else:
            print("Refill successful using profit!")

    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

