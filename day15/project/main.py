MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

treasury = 0


def print_report(in_resources, in_treasury):
    """
    Receives the machine resources and available money
    Prints all of that information for the user
    """
    print(f"""
Resources:
Water: {in_resources["water"]}ml
Milk: {in_resources["milk"]}ml
Coffee: {in_resources["coffee"]}g
Money: ${round(in_treasury, 2)}
""")


def check_resources(in_coffee, in_resources):
    """
    Receives coffee order and available resources
    Returns True if the machine has enough resources to prepare the coffee
    Returns False otherwise
    """
    ingredients = MENU[in_coffee]["ingredients"]
    for ingredient in ingredients:
        print(f"Checking available {ingredient}...")
        if int(ingredients[ingredient]) > in_resources[ingredient]:
            print(f"Sorry, there's not enough {ingredient} to make a {in_coffee}! Refunding...")
            return False
    return True


def take_payment(in_coffee):
    """
    Receives coffee order
    Returns 0 if the user inserted too few coins to cover cost of the order
    Returns the cost of the coffee order if the user paid enough money to cover the cost of the coffee, providing change
    """
    coffee_cost = round(MENU[in_coffee]["cost"], 2)
    print(f"A {in_coffee} costs ${coffee_cost}")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    user_payment = round(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01, 2)

    if user_payment > coffee_cost:
        change = round(user_payment - coffee_cost, 2)
        print(f"Your change: ${change}")
        return coffee_cost
    elif user_payment == coffee_cost:
        return coffee_cost
    else:
        print(f"${user_payment} is not enough money for the requested coffee (${coffee_cost}). Refunding...")
        return 0


def make_coffee(in_coffee):
    """
    Receives the coffee order from the user
    Takes the user's payment, checks that there's enough resources for this coffee order and prepares coffee
    Returns the money made for selling this coffee
    """
    payment = take_payment(in_coffee)
    if payment > 0 and check_resources(in_coffee, resources):
        coffee_ingredients = MENU[in_coffee]["ingredients"]
        for coffee_ingredient in coffee_ingredients:
            resources[coffee_ingredient] -= coffee_ingredients[coffee_ingredient]
        print(f"Here's your {in_coffee}. Enjoy!")
    return payment


# MAIN
keep_running = True
while keep_running:
    selected_option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selected_option == "off":
        print("Turning off the machine.")
        keep_running = False
    elif selected_option == "report":
        print_report(resources, treasury)
    elif selected_option in MENU.keys():
        treasury += make_coffee(selected_option)
    else:
        print("That option doesn't exist! Try again please.")
