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


def check_supplies(ingredients):
    for r in ingredients:
        if ingredients[r] > resources[r]:
            print("Sorry not enough stock in the machine")
            return False
    return True


is_on = True


def make_coffee(ingredients, resources):
    for r in ingredients:

        if ingredients[r] > resources[r]:
            print("Sorry not enough stock in the machine")
            return False
        else:
            resources[r] = resources[r] - ingredients[r]

    print("Here is your coffee!")
    return True

def process_coin():
    print("Please insert coins.")
    total = int(input("How many pennies?")) * 0.01
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many quarters?")) * 0.25

    return total


def check_transaction(cost, payment_balance):
    if cost > payment_balance:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += cost

        if cost < payment_balance:
            change = round(payment_balance - cost, 2)
            print(f"Here is ${change} dollars in change")

        return True


while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input == "off":
        is_on = False
    elif user_input == "report":

        for r in resources:
            if r == "coffee":
                print(f"{str.capitalize(r)}: {resources[r]}g")
                continue
            print(f"{str.capitalize(r)}: {resources[r]}ml")

        print(f"Revenue/Money: ${profit}")

    else:
        drink = MENU[user_input]
        supplies = check_supplies(drink["ingredients"])

        if supplies:
            payment_balance = process_coin()
            print(f"Coin Inserted: ${payment_balance}")

            transaction = check_transaction(drink["cost"], payment_balance)
            if transaction:
                coffee = make_coffee(drink["ingredients"], resources)
