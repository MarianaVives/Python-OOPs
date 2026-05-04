from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
is_on= True

while is_on:
    drink = input(f"Select a drink {menu.get_items()}").lower()
    cost = 0
    print(drink)
    if drink == "report":
        coffee_machine.report()
        money_machine.report()
    elif drink == "off":
        is_on = False

    else:
        beverage = menu.find_drink(drink)
        if coffee_machine.is_resource_sufficient(beverage) and money_machine.make_payment(beverage.cost):
                coffee_machine.make_coffee(beverage)
        else:
            print("We do not have enough resources to prepare your coffee")
