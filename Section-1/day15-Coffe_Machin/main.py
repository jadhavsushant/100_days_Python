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

cash_box = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order):
    """ Loop the resource and check for existing stock and returns true of false"""
    for item in order:
        if order[item] >= resources[item]:
            print(f"“Sorry there is not enough {item}.")
            return False
    return True


def is_transcation_successful(money_received, drink_cost):
    """Return True when payment accepted or False if the money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,  2)
        print(f"Here is ${change} in change")
        global cash_box
        cash_box += drink_cost
        return True
    else:
        print("Sorry, you don't have enough money.  Money refunded")
        return False


def coins_counter():
    """ Return the total value of the inserted coins """
    total = int(input("how may quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.1
    return total


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resource"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


# todo: 1. Prompt user by asking the flavor.
machine_on = True
while machine_on:
    order = input("What would you like?  (espresso/latte/cappuccino): ")
    if order == "off":
        # todo: 7. Turn off the Coffee Machine.
        print("Coffee machine is shutting down")
        machine_on = False

    # todo: 2. Print report resources.
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${cash_box}")

# todo: 3. Check resources sufficient?.
    else:
        brewery = MENU[order]
        if is_resource_sufficient(brewery['ingredients']):
            # todo: 4. Process coins.
            payment = coins_counter()
            # todo: 5. Check transaction successful?
            if is_transcation_successful(payment, brewery['cost']):
                # todo: 6. Make Coffee.
                make_coffee(order, brewery['ingredients'])
