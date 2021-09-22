from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

## TODO 1. Print report
#print(coffee_maker.report())
#print(money_machine.report())
## TODO 2. Check resource sufficient
#print(drink.cost)
#print(drink.name)
#print(drink.ingredients)

## TODO 3. Process coins

## TODO 4. Check transaction successful

## TODO 5. Make Coffee
#coffee_maker.make_coffee(drink)

is_on = True

while is_on:
    drinks = menu.get_items()
    choice = input(f"What would you like to order {drinks}? \n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)
        is_payment_sufficient = money_machine.make_payment(drink.cost)
        if is_resource_sufficient and is_payment_sufficient == True:
            coffee_maker.make_coffee(drink)






