from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

keep_running = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
menu_items = menu.get_items()
while keep_running:
    selected_option = input(f"What would you like? ({menu_items}): ").lower()
    if selected_option == "off":
        print("Turning off the machine.")
        keep_running = False
    elif selected_option == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_order = menu.find_drink(selected_option)
        if coffee_order:
            if coffee_maker.is_resource_sufficient(coffee_order) and money_machine.make_payment(coffee_order.cost):
                coffee_maker.make_coffee(coffee_order)
        else:
            print("That option doesn't exist! Try again please.")
