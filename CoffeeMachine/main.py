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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources_sufficient(ingredients):
    """Determines if we have enough resources to make the drink.
    :param drink: The drink to be made
    :type dict

    :param available: Available resources
    :type dict

    :returns result: is_sufficient, missing_ingredient | None
    :rtype tuple(bool, str | None)
    """
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            return False, ingredient
    return True, None

def process_coins():
    """Processes the total calculated from coins inserted.

    :returns amount: The total amount calculated
    :rtype float
    """
    print("Please insert coins.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

def is_txn_successful(amount_received, drink_cost):
    """Determine if payment is accepted."""
    if drink_cost > amount_received:
        return False
    global profit # profit variable in global scope.
    profit += drink_cost
    change = amount_received - drink_cost
    if change > 0:
        print(f"Here is ${change:.2f} dollars in change.")

    return True

def make_coffee(drink_name, ingredients):
    """Make Coffee"""
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink_name} ☕. Enjoy!")


# TODO: 1. Prompt user for input. Should repeat until users type "off"
running = True
while running:
    keyword = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if keyword == 'off':
        print("Turning off...")
        running = False

    # TODO: 2. Print report by typing the "report" command
    elif keyword == 'report':
        for resource in resources:
            if resource == "coffee":
                unit = "g"
            else:
                unit = "ml"
            print(f"{resource.title()}: {resources[resource]}{unit}")
        print(f"Money: ${profit:.2f}")

    # TODO: 3. When drink selected
    elif keyword in MENU:
        # TODO: 4 check if resources sufficient
        drink_choice = MENU[keyword]
        is_sufficient, lacking = check_resources_sufficient(drink_choice["ingredients"])
        if is_sufficient:
            # TODO: 5. Process coins. quarters, dimes, nickels & pennies.
            amount = process_coins()

            # TODO: 6. Check transaction is successful ?
            if is_txn_successful(amount, drink_choice["cost"]):
                # TODO: 7. Make Coffee
                make_coffee(keyword, drink_choice["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {lacking}")
    else:
        print(f"Sorry, we don't have {keyword}. Please try something on the menu.")
