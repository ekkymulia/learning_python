from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    command = input(f"What would you like to drink ({menu.get_items()}):")

    if command == '':
        break
    elif command == 'off':
        break
    elif command == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        #check supplies
        drink = menu.find_drink(command)
        cs = coffee_maker.is_resource_sufficient(drink)

        #process payment & make drink
        if cs:
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_maker.make_coffee(drink)

